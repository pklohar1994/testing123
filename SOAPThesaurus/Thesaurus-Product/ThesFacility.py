from Thesaurus import Thesaurus
from AccessControl import ClassSecurityInfo, getSecurityManager
from Globals import InitializeClass, DTMLFile, package_home
from Acquisition import Implicit
from Globals import Persistent
from AccessControl.Role import RoleManager
from OFS.SimpleItem import Item
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from OFS.PropertyManager import PropertyManager

import sys, os
import string
import pickle
import re
import xmlrpclib
import types
import time
from os.path import dirname as dr
from copy import deepcopy

from ThesLogger import LoggerFacility
from ThesAccess import AccessFacility

addForm = PageTemplateFile('www/addThesaurus', globals(), __name__='addThesaurus')

# ------------------------------------------------------------------------------
#
# This is the mongo-object version of Thesaurus Product.  I was having issues with
# performance and, after some digging, determined that part of the problem was the
# ZODB and its management of all the object that made up the Thesaurus db. I was
# creating one object per concept (one object per thesaurus term). I switched to
# this one object (one huge object!) to see if I could eliminate the bottleneck
# of thrashing about to pull up the queried-for concept.  It seemed to help.
# Desperate to get the system operational, I've left it in this admittedly
# brain-dead state. It works, albeit updates are maddenly slow as the system has
# to write the mongo-object back to the ZODB. But, read performance is definitely
# better than what I was getting with many (thousands) of little objects.
#
# Need to re-write this from scratch for version 2
#
# ------------------------------------------------------------------------------

reHomograph = re.compile("^[^(]+ [(][^)(]+[)]")
reAsksk = re.compile(" \*$")

#  package_home( globals() )
thePath = "/export/home/tlynch/Thesaurus"
configdir = "config"
schemasdir = "schemas"
sourcedir = "vocabularies"
schema = "thesaurus.schm"
sourcefile = "thesaurus.src"

# some initial values for the logger facility
logsdir = "logs"
logfile = "webservices.log"
loglevel = 3

# general codes
SUCCESS    =   0
NOREQUEST  = 201
NOACCESS   = 202
NOPREF     = 211

# access codes
NOROLE     = 231
SAVEHOSTSFAIL = 232
DELROLEFAIL   = 233
LOADHOSTSFAIL = 234

# logger codes
SETLOGFAIL = 223
GETLOGFAIL = 224
INVLEVEL   = 226
ROTFAIL    = 227

# vocab codes
READSOURCEFAIL = 241
NOSRCFOLDER    = 242

conceptHash = {}
# some initial values for the roles facility
hostsallowfile = "hosts.allow"

def consoles():
   """ return a list of IPs for which we do no hosts.allow checking """
   return ["192.54.138.43", "128.253.101.77", "128.253.87.15", "128.253.87.40"]

def addFunction(dispatcher, id, File=None, Schema=None, REQUEST=None):
   """ add a new thesaurus
       called from the addThesaurus.dtml file """
   T = ThesaurusFacility(id, File, Schema)
   T._loadProperties(package_home(globals()))
   T._initFacilities()
   dispatcher.Destination()._setObject(id, T)
   if REQUEST is not None:
      dispatcher.manage_main(dispatcher, REQUEST)


def canonical(name):
   """ create a canonical form of a term useful for indexing """
   global reAsksk

   name = name.strip().lower()
   name = name.replace(",", "")
   name = name.replace("'", "")
   name = re.sub(reAsksk, "", name)
   name = name.replace("(", "")
   name = name.replace(")", "")
   return name

def decipher(L, term, attr, pos):
   """ an analysis of the term based on it's syntax, attribute, and position """

   # An analysis of the term.
   # If entire term in parentheses, then it is a facet.
   # If part of term is in parentheses, then it's a potential homograph.
   # If trailing asterisk, we can ignore because the attribute describes 
   #  what the trailing asterisk attempts to explain.

   global reHomograph

   term = term.strip()
   what = ""
   scope = ""

   # handle some easy cases first
   if attr in ["DF", "SN"] and pos == 1:
      return {'value':term, 'type':what, 'scope':scope}

   if (term[0] == '(') and (term[len(term) - 1] == ')'):
      what = "facet"
      term = term[1:len(term) -1]
   else:
      if reHomograph.match(term):
         b = term.find('(')
         e = term.find(')')
         scope = term[b + 1:e]
         term = term[0:b - 1]

   return {'value':term, 'type':what, 'scope':scope}


def inlist(list, value):
   """ return the position of value in list, or 0 if it doesn't exist """
   pos = 0
   try:
      pos = list.index(value) + 1
   except ValueError, e:
      pass
   return pos


# end of misc functions
#
# ------------------------------------------------------------------------------

# FYI -- we call InitializeClass at the very end of this file

################################################################################################
################################################################################################

class ThesaurusFacility(Implicit, Persistent, RoleManager, Item, PropertyManager):
   """ create, populate, and manage a thesaurus """

   __implements__ = Thesaurus

   meta_type = 'Thesaurus'

   manage_options = (
      {'label' : 'View',
       'action': 'index_html',
       'help'  : ('Thesaurus', 'view.stx')
       },
      {'label' : 'Properties',
       'action': 'manage_propertiesForm',
       'help'  : ('Thesaurus', 'help.stx')
       },
      {'label' : 'Vocabulary',
       'action': 'manage_vocabulary',
       'help'  : ('Thesaurus', 'vocabulary.stx')
       },
      {'label' : 'Logger',
       'action': 'manage_logger',
       'help'  : ('Thesaurus', 'logger.stx')
       },
      {'label' : 'Access',
       'action': 'manage_laccess',
       'help'  : ('Thesaurus', 'access.stx')
       },
      {'label' : 'WSDL',
       'action': 'manage_wsdl',
       'help'  : ('Thesaurus', 'wsdl.stx')
       },
      ) + RoleManager.manage_options + Item.manage_options

   security = ClassSecurityInfo()

   security.declarePublic('View management screens')
   manage_vocabulary = PageTemplateFile('www/manage_vocabulary', globals(), __name__='manage_vocabulary')

   security.declarePublic('index_html')
   index_html = PageTemplateFile('www/index_html', globals(), __name__='index_html')

   security.declarePublic('results')
   manage_results = PageTemplateFile('www/manage_results', globals(), __name__='manage_results')

   security.declarePublic('manage_configure')
   manage_configure = PageTemplateFile('www/manage_configure', globals(), __name__='manage_configure')

   security.declarePublic('manage_logger')
   manage_logger = PageTemplateFile('www/manage_logger', globals(), __name__='manage_logger')

   security.declarePublic('manage_laccess')
   manage_laccess = PageTemplateFile('www/manage_access', globals(), __name__='manage_laccess')

   security.declarePublic('manage_wsdl')
   manage_wsdl = PageTemplateFile('www/manage_wsdl', globals(), __name__='manage_wsdl')

   security.declarePublic('showTerm')
   manage_showTerm = PageTemplateFile('www/manage_showTerm', globals(), __name__='manage_showTerm')


   def __init__(self, id, file=None, schema=None):
      """ create a new thesaurus """
      self.id = id
      self.title = "Thesaurus Facility"
      self.concepts = {}
      self.names = {}
      self.scopes = {}
      self.attributes = {}
      self.refAttributes = {}
      self.valueAttributes = {}
      self.hierAttributes = {"children":[], "parents":[]}
      self.icpt = 0
      self._properties = ({'id':'title', 'type':'string', 'mode':'w'},)
      self.L = None  # logger
      self.A = None  # Access


   # ------------------------------------------------------------------------------
   #
   # here are some private functions that setup the service and get the daemon thing going
   #

   
   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_loadProperties')
   def _loadProperties(self, thePath):
      """ load Properties from the file-based propertysheet """

      # We expect a file named 'configure' in the Products/Thesaurus
      # thePath is set to Products/Thesaurus
      configure = "%s/configure" % thePath

      # I hacked OFS/PropertManager/_setProperty to accept the mode attribute
      mode = 'w'
      try:
         lines = file(configure).readlines()
      except:
         raise 'Bad Path', "Invalid path to configure file: %s" % configure

      if self.hasProperty('thePath'):
         self._updateProperty('thePath', thePath)
      else:
         self._setProperty('thePath', thePath, 'string', mode=mode)

      intext = 0
      for line in lines:
         cont = line[0]
         line = line[1:]
         line = line.strip()

         if cont == " ":  # SPACE indicates a new, not contuation, line
            if intext:
               if self.hasProperty(prop):
                  self._updateProperty(prop, value)
               else:
                  self._setProperty(prop, value, type)
               intext = 0
            (prop, type, value) = line.split(":",2)
            if type == 'text':
               intext = 1
               value = "%s\n" % value
            else:
               if type == 'lines':
                  value = eval(value)
               if self.hasProperty(prop):
                  self._updateProperty(prop, value)
               else:
                  self._setProperty(prop, value, type, mode=mode)
         else:                                         # else it's a continuation line
            value = "%s%s\n" % (value, line)

      if intext:
         if self.hasProperty(prop):
            self._updateProperty(prop, value)
         else:
            self._setProperty(prop, value, type, mode=mode)


      if self.hasProperty('wsdl_file'):
         try:
            wsdl_file_path = "%s/config/%s" % (self.thePath, self.wsdl_file)
            self.wsdlschema = file(wsdl_file_path).readlines()
         except:
            raise 'Bad wsdl_file_path', 'bad path: %s' % wsdl_file_path

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_initFacilities')
   def _initFacilities(self):
      """ initialize the Logger and Access sub-systems """
      # Get ready to do some work
      # initialize the logger sub-system
      self._initLoggerFacility('logger')
      # initialize the Access/Roles sub-system
      self._initAccessFacility('roles')
     
   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_initLoggerFacility')
   def _initLoggerFacility(self, id):
      """ initialize the logger facility """
      self.L = LoggerFacility(id)
      self.L._initLogger(self)
      self.L._setlogging()
      self.L._writeLog("initLoggerFacility", ['OK',''], [], [], "daemon", 1)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_initAccessFacility')
   def _initAccessFacility(self, id):
      """ initialize the access facility """
      self.A = AccessFacility(id)
      self.A._initAccess(self)
      self.L._setAccessRef(self.A)
      self.A._setLoggerRef(self.L)
      self.A._readHostsAllow()
      self.L._writeLog("_initAccessFAcility", ['OK', ""], [], [], "daemon", 2)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_refreshProperties')
   def _refreshProperties(self, updates=None):
      """ get a fresh copy of the Thesaurus folder properties """

      if not updates:
         self.theProperties = {}

         for (id, P) in self.propertyItems():
            self.theProperties[id] = P
      else:
         self.manage_changeProperties(updates)

      return self.theProperties


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('refreshProperties')
   def refreshProperties(self):
      """ get a fresh copy of the Thesaurus folder properties """

      return self.theProperties


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_readSchema')
   def _readSchema(self, schema=None):
      """ read the schema file holding valid attributes """

      self._refreshProperties()

      if not schema:
         schema = self.theProperties['schema']
      configdir = self.theProperties['configdir']
      schemadir = self.theProperties['schemadir']
      thePath = self.theProperties['thePath']

      schema = "%s/%s/%s/%s" % (thePath, configdir, schemadir, schema)
      try:
         lines = file(schema).readlines()
      except:
         self.L._writeLog('_readSchema', ["FAIL", "could not load schema file %s" % schema], [], [], "daemon", 1)
         return 0
         

      self.attributes = {}
      self.refAttributes = {}
      self.valueAttributes = {}
      self.hierAttributes = {}
      for line in lines:
         if line[0] == '#' or line[0] == '\n':
            continue
         line = line.strip()
         try:
            (tag, label, indexed, direction) = line.split(':')
         except:
            try:
               (tag, label, indexed) = line.split(':')
               direction = ""
            except:
               continue
         tag = tag.strip().lower()
         label = label.strip()
         direction = direction.strip().lower()
         indexed = int(indexed)
         self.attributes[tag] = label
         if indexed == 1:
            self.refAttributes[tag] = label
         else:
            self.valueAttributes[tag] = label
         if direction:
            if not self.hierAttributes.has_key(direction):
               self.hierAttributes[direction] = []
            self.hierAttributes[direction].append(tag)

      self.L._writeLog('_readSchema', ["OK", "loaded attributes file %s" % schema], [], [], "daemon", 1)
      self._p_changed = 1
      return 1


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_readThesaurusSource')
   def _readThesaurusSource(self, sourcefile=None, sourcedir=None, thePath=None, REQUEST=None):
      """ read an ASCII version of the thesaurus """


      if not REQUEST and (not sourcedir or not thePath or not sourcefile):
         return 0

      self._refreshProperties()

      if REQUEST.has_key('sourcefile'):
         sourcefile = REQUEST['sourcefile']
      if REQUEST.has_key('sourcedir'):
         sourcedir = REQUEST['sourcedir']
      if REQUEST.has_key('thePath'):
         thePath = REQUEST['thePath']
      if REQUEST.has_key('loadreport'):
         loadreport = REQUEST['loadreport']

      if not sourcedir:
         sourcedir = self.theProperties['sourcedir']
      if not thePath:
         thePath = self.theProperties['thePath']
      if not sourcefile:
         sourcefile = self.theProperties['sourcefile']

      loadreport = self.theProperties['loadreport']
      logsdir = self.theProperties['logsdir']

      if loadreport == "":
         loadreport = "/dev/null"

      # we dump a detailed record to a separate file
      ldrprt = open("%s/%s/%s" % (thePath, logsdir, loadreport), 'w')
      ldrprtHeader = """ Load Report

This report details the loading of the vocabulary.

Note:  Errors are indicated by a line beginning with ERROR

--- Section 1 ---

Schema

"""
      ldrprt.write(ldrprtHeader)
      if self.refAttributes == {} and self.valueAttributes == {}:
         self.L._writeLog('_readThesaurusSource', ["OK", "attempting to load schema"], [], [], "daemon", 1)
         self._readSchema()

      ldrprt.write("schema: %s\nref attributes:\n" % self.theProperties['schema'])
      for k in self.refAttributes.keys():
         ldrprt.write("%s: %s\n" % (k, self.refAttributes[k]) )
      ldrprt.write("value attributes:\n")
      for k in self.valueAttributes.keys():
         ldrprt.write("%s: %s\n" % (k, self.valueAttributes[k]))
      ldrprt.write("hier attributes:\n")
      for k in self.hierAttributes.keys():
         ldrprt.write("%s: " % k)
         for v in self.hierAttributes[k]:
            ldrprt.write("%s, " % v)
         ldrprt.write("\n")

      sourcefile = os.path.basename(sourcefile)
      filename = "%s/%s/%s" % (thePath, sourcedir, sourcefile)
      try:
         lines = file(filename).readlines()
      except:
         self.L._writeLog('_readThesaurusSource', ["FAIL", "could not open sourcefile %s" % filename], [], [], "daemon", 1)
         ldrprt.close()
         return READSOURCEFAIL

      self.L._writeLog('_readThesaurusSource', ["OK", "saving load report in %s" % loadreport], [], [], "daemon", 1)
      self.concepts = {} 
      self.names = {}
      self.scopes = {}

      ldrprtSec2 = """

--- Section 2 ---

Vocabulary

"""
      ldrprt.write(ldrprtSec2)
      for line in lines:
         if line[0] == '#' or line[0] == '\n':
            continue
         line = line.strip()
         (left, attr, right) = line.split('\t')
         # add all left-side terms as we encounter them
         stuff = decipher(self.L, left, attr, 0)
         n = self._addTerm(stuff, ldrprt)

         # Add right-side terms if not a definition or scope-note as we need to
         # find a reference to the right-side term when adding attribute to left term.
         stuff = decipher(self.L, right, attr, 1)
         if not attr in ["DF", "SN"]:
            self._addTerm(stuff, ldrprt)
         self._addAttribute(n, attr, stuff, ldrprt)

      ldrprt.close()
      self.L._writeLog('_readThesaurusSource', ["OK", "done processing sourcefile %s" % filename], [], [], "daemon", 1)
      if sourcefile != self.theProperties['sourcefile']:
         self._refreshProperties({'sourcefile':sourcefile})
      self._p_changed=1
      return 1


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_addTerm')
   def _addTerm(self, stuff, ldrprt):
      """ add a new term and initialize it """
      # check to see if we already have this name/scope
      name = stuff['value']
      cname = canonical(name)
      scope = stuff['scope']
      if len(scope) > 1:
         if scope[len(scope) - 1] == ")":
            scope = scope[:-1]
      cscope = canonical(scope)
      if self.scopes.has_key((cname,cscope)):   # index on name/scope tuple
         return self.scopes[(cname,cscope)]

      # new name/scope 
      n = self.icpt
      self.icpt = self.icpt + 1
      self.concepts[n] = {'name':name}
      if stuff['scope'] != "":
         self.concepts[n]['scope'] = scope
      if stuff['type'] != "":
         self.concepts[n]['type'] = stuff['type']
      # we keep two inverted indexes: scopes and names
      # scopes is unique and is a quick lookup of a concept if we have both name and scope
      # names is not guaranteed to be unique, but often all we have is the name
      self.scopes[(cname,cscope)] = n
      if self.names.has_key(cname):
         self.names[cname].append(n)
      else:
         self.names[cname] = [n]
      ldrprt.write("added Term: (%d) name: %s, scope: %s\n" % (n, name, scope))
      return n


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_addAttribute')
   def _addAttribute(self, n, attribute, stuff, ldrprt):
      """ add an attribute to the concept """
      # some attributes are simply added to concept
      # others are added as reference to another concept

      value = stuff['value']
      cname = canonical(value)
      scope = stuff['scope']
      if len(scope) > 1:
         if scope[len(scope) - 1] == ")":
            scope = scope[:-1]
      cscope = canonical(scope)
      what = stuff['type']
      attribute = attribute.lower()

      if attribute in self.valueAttributes.keys():
         # first, do those that are directly added
         if not self.concepts[n].has_key(attribute):
            self.concepts[n][attribute] = [value]
            ldrprt.write("added attribute: %s %s for %s (%s)\n" % (attribute, value, cname, cscope))
         else:
            if not inlist(self.concepts[n][attribute], value):
               self.concepts[n][attribute].append(value)
               ldrprt.write("appended attribute: %s %s for %s (%s)\n" % (attribute, value, cname, cscope))
      elif attribute in self.refAttributes.keys():
         # handle those attributes added as ref
         ref = self.scopes[(cname,cscope)]
         if not self.concepts[n].has_key(attribute):
            self.concepts[n][attribute] = [ref]
            ldrprt.write("added attribute: %s %s for %s (%s)\n" % (attribute, value, cname, cscope))
         else:
            self.concepts[n][attribute].append(ref)
            ldrprt.write("appended attribute: %s %s for %s (%s)\n" % (attribute, value, cname, cscope))
      else:
         ldrprt.write("ERROR :: missing term or attribute: value: |%s| cname: |%s| cscope: |%s| attribute: |%s|\n" % (value, cname, cscope, attribute))


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getServices')
   def _getServices(self):
      """ return a dict of services and associated roles """
     
      # these are the services that are security.declarePublic 
      services = { 'getTerm' : 'browser',
            'findTerms' : 'browser',
            'findPreferred' : 'browser',
            'searchForConcepts' : 'user',
            'fetchConcepts' : 'user',
            'fetchHier' : 'user',
            'myRole' : 'user',
            'verifyIP' : 'operator',
            'tailLog' : 'operator',
            'reportLogStatus' : 'operator',
            'logMessage' : 'operator',
            'rotateLogFile' : 'operator',
            'setLogging' : 'admin',
            'setLogDefault' : 'admin',
            'readHostsAllow' : 'admin',
            'getHostsAllow' : 'admin',
            'readSourceFile' : 'admin',
            'loadOnCron' : 'admin',
            'loadSource' : 'admin',
            'getServices' : 'admin'}
      return services


   # here are some interfaces to the Access Facility 
   security.declarePublic('verifyIP')
   def verifyIP(self, ip, REQUEST=None):
      """ interface to Access Facility's verify IP """
      return self.A.verifyIP(ip, REQUEST)

   security.declarePublic('addHostwithRole')
   def addHostwithRole(self, host=None, role=None, REQUEST=None):
      """ interface to Access Facility's addHostwithRole """
      return self.A.addHostwithRole(host, role, REQUEST)

   security.declarePublic('deleteHostwithRole')
   def deleteHostwithRole(self, host=None, role=None, REQUEST=None):
      """ interface to Access Facility's deleteHostwithRole """
      return self.A.deleteHostwithRole(host, role, REQUEST)

   security.declarePublic('getHostsAllow')
   def getHostsAllow(self, REQUEST=None):
      """ interface to Access Facility's getHostsAllow """
      return self.A.getHostsAllow(REQUEST)

   security.declarePublic('myRole')
   def myRole(self, REQUEST=None):
      """ interface to Access Facility's myRole """
      return self.A.myRole(REQUEST)

   security.declarePublic('readHostsAllow')
   def readHostsAllow(self, REQUEST=None):
      """ interface to Access Facility's readHostsAllow """
      return self.A.readHostsAllow(REQUEST)


   # here are some interfaces to the Logger Facility
   security.declarePublic('reportLogStatus')
   def reportLogStatus(self, REQUEST=None):
      """ interface to Logger Facility's reportLogStatus """
      res = self.L.reportLogStatus(REQUEST)[0]
      logfile = os.path.basename(res[0])
      logdir = os.path.basename(os.path.dirname(res[0]))
      return ("%s/%s" % (logdir, logfile), res[1])

   security.declarePublic('logMessage')
   def logMessage(self, who, msg, level=None, REQUEST=None):
      """ interface to Logger Facility's logMessage """
      return self.L.logMessage(who, msg, level, REQUEST)

   security.declarePublic('rotateLogFile')
   def rotateLogFile(self, REQUEST=None):
      """ interface to Logger Facility's rotateLogFile """
      return self.L.rotateLogFile(REQUEST)

   security.declarePublic('setLogging')
   def setLogging(self, logfilename=None, level=None, REQUEST=None):
      """ interface to Logger Facility's setLogging """
      return self.L.setLogging(logfilename, level, REQUEST)

   security.declarePublic('setLogDefault')
   def setLogDefault(self, filename=None, REQUEST=None):
      """ interface to Logger Facility's setLogDefault """
      return self.L.setLogDefault(filename, REQUEST)

   security.declarePublic('tailLog')
   def tailLog(self, lines=10, REQUEST=None):
      """ interface to Logger Facility's tailLog method """
      return self.L.tailLog(lines, REQUEST)

   # ------------------------------------------------------------------------------
   #
   # Beginning here are some methods that create a browser interface to the thesaurus
   # These services are the legacy browser interface that was developed as part of the
   # prototype. 
   #
   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('getTerm')
   def getTerm(self, expression, REQUEST=None):
      """ find the term that matches the expression """

      expression = canonical(expression)

      self.L._writeLog('getTerm', ["OK", "browser"], [expression], [], REQUEST['REMOTE_ADDR'], 1)

      REQUEST['matches'] = []
      if not expression or 0 == len(expression):
         self.L._writeLog('getTerm', ["FAIL", "browser"], [expression], [], REQUEST['REMOTE_ADDR'], 2)
         return self.results(REQUEST)

      res = self._getConceptByScopeWithValues((expression, ""))

      if res[1] == 0:
         i = expression.find('(')
         if i > 0:
            scope = expression[i+1:-1]
            name = expression[0:i-1]
            res = self._getConceptByScopeWithValues((name, scope))
            if res[1] == 0:
               self.L._writeLog('getTerm', ["FAIL", "browser"], [expression], [], REQUEST['REMOTE_ADDR'], 2)
               return self.results(REQUEST)
            

      REQUEST['matches'] = res[0]

      self.L._writeLog('getTerm', ["OK", "browser"], [expression], [], REQUEST['REMOTE_ADDR'], 2)
      return self.manage_showTerm(REQUEST)

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('findTerms')
   def findTerms(self, expression, REQUEST=None):
      """ find all terms that match expression """

      self.L._writeLog('findTerms', ["OK", "browser"], [expression], [], REQUEST['REMOTE_ADDR'], 1)

      expression = canonical(expression)
      if not expression or 0 == len(expression):
         return self.results(REQUEST)

      REQUEST['matches'] = []
      for l in range(0,4):
         res = self._locateConcepts(expression, l)
         if res[1] == 1:
            break
      else:
         self.L._writeLog('findTerms', ["FAIL", "browser"], [expression], [], REQUEST['REMOTE_ADDR'], 2)
         return self.results(REQUEST)

      if len(res[0]) > 0:
         for c in res[0]:
            r = self._getConceptByIndxDpCy(c)
            name = r[0]['name']
            if r[0].has_key('scope'):
               scope = r[0]['scope']
               name = "%s (%s)" % (name, scope)
            REQUEST['matches'].append(name)
         (REQUEST['matches']).sort()
         self.L._writeLog('findTerms', ["OK", "browser"], [expession], [], REQUEST['REMOTE_ADDR'], 2)
      else:
         self.L._writeLog('findTerms', ["FAIL", "browser"], [expression], [], REQUEST['REMOTE_ADDR'], 2)

      return self.manage_results(REQUEST)

   #
   # end the browser interface methods
   # ------------------------------------------------------------------------------

   # ------------------------------------------------------------------------------
   #
   # web services are defined below this point
   #
   # tlynch@nal.usda.gov
   #
   # February 15, 2003
   #


   # first we have some private functions 
   # these private fucntions do the heavy lifting

   # names of private functions typically begin with an underscore

   # private functions either return a Boolean true/false, or a two element array:
   #  - element 0 holds results
   #  - element 1 holds 0:failure or 1:success
   # results are typically an array of concepts or terms


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_info')
   def _info(self):
      """ return some standard verbage about this service """
      # the about property is of type text. What we need to do is convert
      # text lines to an array
      return eval("%s" % self.theProperties['about'].split('\n') )


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_locateConcepts')
   def _locateConcepts(self, term, level):
      """ attempt to locate terms in database, using indicated level of wildcarding """

      # level sets the degree of wildcarding we will do
      # level 0 -- no wildcarding
      # level 1 -- add or remove a trailing s or es
      # level 2 -- try a suffix regex search
      # level 3 -- try a prefix regex search
      # level 4 -- try both prefix and suffix regex search

      # We return an array of two elements:
      #
      # The first element is itself an array of indexes of matching concepts.
      #
      # The second element is a one or zero indicating success or failure
      # of the method call.  Supplying an invalid level, for example, would
      # cause the method to return failure.  Not finding a valid term
      # also returns a 0.


      level = int(level)
     
      res = {}
      response = []
      status = 0

      if level < 0 or 4 < level:
         return [response, 0]

      cterm = canonical(term) 

      # do first check for any level
      if self.names.has_key(cterm):
         response = self.names[cterm]
         status = 1
   
      if level > 0:
         n = len(cterm) - 1

         if cterm[n] != "s":
            cterms = cterm + "s"
            if self.names.has_key(cterms):
               response = response + self.names[cterms]
               status = 1
  
            ctermes = cterm + "es"
            if self.concepts.has_key(ctermes):
               response = response + self.names[ctermes]
               status = 1
   
         if cterm[n] == "s":
            if cterm[n - 1] == "e":
               n = n - 1
               cterm = cterm[0:n]
               if self.names.has_key(cterm):
                  response = response + self.names[cterm]
                  status = 1

      # time to get serious
      #
      # a term might consist of several words, so for each word,
      # we will do some cheap stemming and build a regex expression
      # I considered a more serious stemming algorithm like the Porter
      # algorithm, but in the end, decided that for the terms I'm dealing
      # with, the simple algorithm below works well.
      if level > 1:
         cterm = canonical(term)
         p2 = re.compile("^%s.*$" % cterm,   re.IGNORECASE)
         p3 = re.compile("^.*%s$" % cterm,   re.IGNORECASE)
         p4 = re.compile("^.*%s.*$" % cterm, re.IGNORECASE)
         matches = []

      if level == 2:
         for trm in (self.names).keys():
            if p2.match(trm):
               response = response + self.names[trm]

      if level ==  3:
         for trm in (self.names).keys():
            if p3.match(trm):
               response = response + self.names[trm]

      if level == 4:
         for trm in (self.names).keys():
            if p4.match(trm):
               response = response + self.names[trm]

      for i in response:
         res[i] = 1
      if len(res.keys()) > 0:
         status = 1
      return [res.keys(), status]


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getConceptByIndxDpCy')
   def _getConceptByIndxDpCy(self, indx):
      """ get the concept with indx """

      # used by findTerms and for findTerms we need deepcopy

      try:
         indx = int(indx)
      except:
         return [{}, 0]
      if not self.concepts.has_key(indx):
         self.L._writeLog('_getConceptByIndxDpCy', ["FAIL", "invalid index: %d" % indx], [str(indx)], [], "daemon", 2)
         return [{}, 0]

      concept = deepcopy(self.concepts[indx])
      return [concept, 1]


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getConceptByIndx')
   def _getConceptByIndx(self, indx):
      """ get the concept with indx """

      try:
         indx = int(indx)
      except:
         return [{}, 0]
      if not self.concepts.has_key(indx):
         self.L._writeLog('_getConceptByIndx', ["FAIL", "invalid index: %d" % indx], [str(indx)], [], "daemon", 2)
         return [{}, 0]

      return [self.concepts[indx], 1]


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getAttrByIndx')
   def _getAttrByIndx(self, indx, attr):
      """ get the attribute associated with concept with indx """

      try:
         indx = int(indx)
      except:
         return []
      if not self.concepts.has_key(indx):
         self.L._writeLog('_getAttrByIndx', ["FAIL", "invalid index: %d" % indx], [str(indx)], [], "daemon", 2)
         return []

      if not self.concepts[indx].has_key(attr):
         self.L._writeLog('_getAttrByIndx', ["FAIL", "no attr: %s" % attr], [str(indx)], [], "daemon", 2)
         return []

      return self.concepts[indx][attr]


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getIndxByScope')
   def _getIndxByScope(self, term):
      """ get the concept as specified by name and scope """

      # presumption is we have a valid term that does indeed exist in the db
      # term is actually a tuple holding both name and scope

      (name, scope) = term
      name = canonical(name)
      scope = canonical(scope)
     
      if not self.scopes.has_key((name, scope)):
         self.L._writeLog('_getIndxByScope', ["FAIL", "invalid name %s or scope |%s|" % (name, scope)], [term], [], "daemon", 2)
         return [{}, 0]
      else: 
         return [self.scopes[(name,scope)], 1]


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getConceptByScope')
   def _getConceptByScope(self, namescope):
      """ get the concept as specified by name and scope """

      # presumption is we have a valid term that does indeed exist in the db
      # term is actually a tuple holding both name and scope

      (name, scope) = namescope
      name = canonical(name)
      scope = canonical(scope)
     
      if not self.scopes.has_key((name, scope)):
         self.L._writeLog('_getConceptByScope', ["FAIL","invalid cname: %s or cscope: %s" % (name, scope)], [], [], "daemon", 2)
         return [{}, 0]
      else: 
         concept = deepcopy(self.concepts[self.scopes[(name,scope)]])
         concept['index'] = self.scopes[(name,scope)]
         return [concept, 1]


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getConceptByScopeWithValues')
   def _getConceptByScopeWithValues(self, term):
      """ get the concept with values as specified by name/scope """

      nconcept = {}
      try:
         (name, scope) = term
         res = self._getIndxByScope((name, scope))
         if res[1] == 0:
            self.L._writeLog('_getConceptByScopeWithValues', ["FAIL", "invalid name %s or scope %s" % (name, scope)], [term], [], "daemon", 2)
            return [{}, 0]

         concept = deepcopy(self.concepts[res[0]])
         for k in concept.keys():
            if not k in self.refAttributes.keys():
               nconcept[k] = deepcopy(concept[k])
            else:
               nconcept[k] = []
               for n in concept[k]:
                  namescope = {'name':'', 'scope':''}
                  if self.concepts[n].has_key('name'):
                     namescope['name'] = self.concepts[n]['name']
                  if self.concepts[n].has_key('scope'):
                     namescope['scope'] = self.concepts[n]['scope']
                  nconcept[k].append(namescope)
         nconcept['index'] = str(res[0])
         return [nconcept, 1]
      except:
         self.L._writeLog('_getConceptByScopeWithValues', ["FAIL", "invalid name/scope"], [term], [], "daemon", 2)
         return [{}, 0]


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getConceptByIndxWithValues')
   def _getConceptByIndxWithValues(self, indx):
      """ given index of concept, find the associated values, or words, referenced by the indices """

      nconcept = {}
      try:
         indx = int(indx)

         concept = self.concepts[indx]

         for k in concept.keys():
            if not k in self.refAttributes.keys():
               nconcept[k] = deepcopy(concept[k])
            else:
               nconcept[k] = []
               for n in concept[k]:
                  namescope = {'name':'', 'scope':''}
                  if self.concepts[n].has_key('name'):
                     namescope['name'] = self.concepts[n]['name']
                  if self.concepts[n].has_key('scope'):
                     namescope['scope'] = self.concepts[n]['scope']
                  nconcept[k].append(namescope)
         nconcept['index'] = str(indx)
         return [nconcept, 1]
      except:
         try:
            indx = str(indx)
            self.L._writeLog('_getConceptByIndxWithValues', ["FAIL", "a) invalid index"], [str(indx)], [], "daemon", 2)
         except:
            self.L._writeLog('_getConceptByIndxWithValues', ["FAIL", "b) invalid index"], [str(indx)], [], "daemon", 2)
         return [{}, 0]


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getConceptByIndxWithout')
   def _getConceptByIndxWithout(self, indx, direction):
      """ given index of concept, find the associated values, or words, referenced by the indices 
          except for the attributes referrenced by direction """

      nconcept = {}
      try:
         indx = int(indx)

         concept = self.concepts[indx]

         for k in concept.keys():
            if (not k in self.refAttributes.keys()) or (k in direction):
               nconcept[k] = deepcopy(concept[k])
            else:
               nconcept[k] = []
               for n in concept[k]:
                  namescope = {'name':'', 'scope':''}
                  if self.concepts[n].has_key('name'):
                     namescope['name'] = self.concepts[n]['name']
                  if self.concepts[n].has_key('scope'):
                     namescope['scope'] = self.concepts[n]['scope']
                  nconcept[k].append(namescope)
         nconcept['index'] = str(indx)
         return [nconcept, 1]
      except:
         try:
            indx = str(indx)
            self.L._writeLog('_getConceptByIndxWithout', ["FAIL", "a) invalid index"], [str(indx)], [], "daemon", 2)
         except:
            self.L._writeLog('_getConceptByIndxWithout', ["FAIL", "b) invalid index"], [str(indx)], [], "daemon", 2)
         return [{}, 0]


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getConceptScope')
   def _getConceptScope(indx):
      """ return name/scope for indx """


      namescope = {'name':'', 'scope':''}
      if not self.concepts.has_key(int(indx)):
         return namescope

      namescope['name'] = self.concepts['name']
      if self.concepts[indx].has_key('scope'):
         namescope['scope'] = self.concepts[indx]['scope']

      return namescope

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getConceptHash')
   def _getConceptHash(self, index, level, direction, depth=0):
      """ recursively create a single dimensional array of concepts 
          to desired depth in broader/narrower hierarchy """

      global conceptHash

      level = int(level)
      if (depth >= level):  # we're done. Note that level == 0 means go as far as possible
         conceptHash[index] = index
         return

      concept = self._getConceptByIndx(index)[0]

      attrs = [item for item in direction if concept.has_key(item)]  # direction == ['bt','ct'] or ['nt','cn']
   
      if (not attrs):  # at end of hierarchy
         conceptHash[index] = index
         return

      for attr in attrs: # attrs is ['bt', 'ct'] or ['nt', 'cn']
         for idx in concept[attr]:
            self._getConceptHash(idx, level, direction, (depth + 1))

      return


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getComplex')
   def _getComplex(self, complx, level, direction, depth=0):
      """ recursively create the complex concept object """
  
      level = int(level) 
      attrs = [item for item in direction if complx.has_key(item)]
   
      if (not attrs) or (not (level == 0 or depth <= level)):
         res = {'name':complx['name'], 'scope':''}
         if complx.has_key('scope'):
            res['scope'] = complx['scope']
         return res

      newAttrLists = {}             # tmp holding area to gather results
      for attr in attrs:            # something like ['bt', 'ct']
         newAttrLists = []
         for idx in complx[attr]:
            newComplx = self._getConceptByIndxWithout(idx, direction)[0]
            thisC = self._getComplex(newComplx, level, direction, (depth + 1))
            if thisC:
               newAttrLists.append(thisC)
      
         complx[attr] = deepcopy(newAttrLists)
   
      return complx


   # end of the private functions section
   #
   #
   # ------------------------------------------------------------------------------

   # ------------------------------------------------------------------------------
   # 
   # Now for the Public Methods of the Thesaurus web service.
   # Public methods are careful to check remote IP and validate against hosts.allow.

   # First we define the those Public Methods intended for use by clients with 'user' access

   
   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('searchForConcepts')
   def searchForConcepts(self, termList=None, level=None, REQUEST=None):
      """ for each term in the list termList call _locateConcepts """

      # a public interface to the _locateConcepts function

      results = {'concepts':[], 'statusCode':201}
      if not REQUEST and not termList:
         return {'results':results}


      if not level:
         level = 0

      # debug - tjl
      if termList:
         if type(termList) == type(""):
            termList = [termList]


      if hasattr(REQUEST, 'isSOAP'):   # soap invocation, find args in REQUEST object
#         termList = None
         kw = getattr(REQUEST, 'kwargs')
         if kw.has_key('termList'):
            termList = kw['termList']
         if kw.has_key('level'):
            level = kw['level']

      if not termList:
         self.L._writeLog('searchForConcepts', ["FAIL", "no termList"], [], [], "", 2)
         results = {'concepts':[], 'statusCode':211}
         return {'results':results}

      if not REQUEST:
         self.L._writeLog('searchForConcepts', ["FAIL", "no REQUEST"], [], [], "", 2)
         results = {'concepts':[], 'statusCode':212}
         return {'results':results}

      if not REQUEST.has_key('REMOTE_ADDR'):
         self.L._writeLog('searchForConcepts', ["FAIL", "no REQUEST[REMOTE_ADDR]"], [], [], "", 2)
         results = {'concepts':[], 'statusCode':213}
         return {'results':results}

#      if not self.A._allowed('user', REQUEST['REMOTE_ADDR']):
#         self.L._writeLog('searchForConcepts', ["FAIL", "invalid address"], termList, [], REQUEST['REMOTE_ADDR'], 2)
#         return {'results' : {'concepts':[], 'statusCode':202}}

      if type(termList) == type(""):
         termList = [termList]
      level = int(level)
      if level < 0 or 5 < level:
         self.L._writeLog('searchForConcepts', ["FAIL", "invalid level %d" % level], termList, [], REQUEST['REMOTE_ADDR'], 2)
         return {'results' : {'concepts':[], 'statusCode':204}}

      response = []
      indxList = []
      b = level
      e = level+1
      if level == 5:
         b = 0
         e = 5
      for term in termList:
         for level in range(b,e):
            results = self._locateConcepts(term, level)
            if results[1] != 0:
               indxList = indxList + results[0]
               break

      for indx in indxList:
         res = self._getConceptByIndxWithValues(indx)
         if res[1] == 1:
            response.append(res[0])

      self.L._writeLog('searchForConcepts', ["OK", ""], termList, [], REQUEST['REMOTE_ADDR'], 2)
      return {'results':{'concepts':response, 'statusCode':0}}

   
   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('wsdl')
   def wsdl(self, REQUEST=None):
      """ wsdl returns the WSDL description file for these services """
     
      if REQUEST == None:
         return {'wsdlResponse':"", 'statusCode':201}
      # we don't bother with security check here as the wsdl is open to the world
      
      return self.wsdl


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('fetchHier')
   def fetchHier(self, nameScope=None, level=None, direction=None, REQUEST=None):
      """ fetch either the parents or children of indx to specified level """

      global conceptHash

      if nameScope == None or level == None or direction == None or not REQUEST:
         return {'results':{'concepts':[], 'statusCode':201}}

      if hasattr(REQUEST, 'isSOAP'):   # soap invocation, find args in REQUEST object
#         termList = None
         kw = getattr(REQUEST, 'kwargs')
         if kw.has_key('nameScope'):
            nameScope= kw['nameScope']
         if kw.has_key('level'):
            level = kw['level']
         if kw.has_key('direction'):
            direction = kw['direction']

      try:
         level = int(level)
      except:
         self.L._writeLog('fetchHier', ["FAIL", "invalid value for level %s" % str(level)], [str(nameScope)], [], REQUEST['REMOTE_ADDR'],  2)
         return {'results':{'concepts':[], 'statusCode':203}}

      scope = ''
      try:
         name = getattr(nameScope, 'name')
      except:
         try:
            name = nameScope['name']
            if nameScope.has_key('scope'):
               scope = nameScope['scope']
         except:
            self.L._writeLog('fetchHier', ["FAIL", "cannot access nameScope: type(nameScope) = %s" % type(nameScope)], [str(nameScope)], [], REQUEST['REMOTE_ADDR'],  2)
            return {'results':{'concepts':[], 'statusCode':203}}
      else:
         scope = getattr(nameScope, 'scope')

      r = self._getConceptByScope((name, scope))
      if r[1] == 0:
         return {'results':{'concepts':[], 'statusCode':203}}

      conceptHash = {}
      self._getConceptHash(int(r[0]['index']), level, self.hierAttributes[direction],0)
      if conceptHash == {}:
         return {'results':{'concepts':[], 'statusCode':203}}

     
      conceptArray = []
      for k in conceptHash.keys():
         conceptArray.append(self._getConceptByIndxWithValues(k)[0])
      return {'results':{'concepts':conceptArray, 'statusCode':0}}



   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('hierFetch')
   def hierFetch(self, nameScope=None, level=None, direction=None, REQUEST=None):
      """ fetch either the parents or children of indx to specified level """

      if nameScope == None or level == None or direction == None or not REQUEST:
         return {'hierFetchResponse':[], 'statusCode':201}


      try:
         level = int(level)
      except:
         self.L._writeLog('hierFetch', ["FAIL", "invalid value for level %s" % str(level)], [str(nameScope)], [], REQUEST['REMOTE_ADDR'],  2)
         return {'hierFetchResponse':[], 'statusCode':203}

      try:
         if not self.A._allowed('user', REQUEST['REMOTE_ADDR']):
            self.L._writeLog('hierFetch', ["FAIL", "invalid address"], [str(nameScope)], [], REQUEST['REMOTE_ADDR'], 2)
            return {'hierFetchResponse':[], 'statusCode':213}
      except:
         self.L._writeLog('hierFetch', ["FAIL", "no ip address"], [str(nameScope)], [], REQUEST['REMOTE_ADDR'],  2)
         return {'hierFetchResponse':[], 'statusCode':223}

      try:
         name = getattr(nameScope, 'name')
      except:
         return {'hierFetchResponse':[], 'statusCode':233}

      try:
         scope = getattr(nameScope, 'scope')
      except:
         scope = ''

      r = self._getConceptByScope((name, scope))     # fix this so I can call getConceptByIndxWithout directly - tjl
      if r[1] == 0:
         return {'hierFetchResponse':[], 'statusCode':200}
      newComplx = self._getConceptByIndxWithout(int(r[0]['index']), self.hierAttributes[direction])[0]

      response = self._getComplex(newComplx, level, self.hierAttributes[direction])
      if response == {}:
         return {'hierFetchResponse':[], 'statusCode':210}

      return {'hierFetchResponse':response, 'statusCode':0}


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('fetchConcepts')
   def fetchConcepts(self, nameScopeList=None, attributes=None, REQUEST=None):
      """ for each term in the list nameScopeList call _getConceptByScopeWithValues """

      if not nameScopeList:
         return {'results':{'concepts':[], 'statusCode':201}}
      if not REQUEST:
         return {'results':{'concepts':[], 'statusCode':201}}
      if not REQUEST.has_key('REMOTE_ADDR'):
         return {'results':{'concepts':[], 'statusCode':201}}



      if hasattr(REQUEST, 'isSOAP'):   # soap invocation, find args in REQUEST object
         kw = getattr(REQUEST, 'kwargs')
         if kw.has_key('nameScopeList'):
            nameScopeList = kw['nameScopeList']
         if kw.has_key('attributes'):
            attributes = kw['attributes']

      if type(nameScopeList) == type(""):
         nameScopeList = [nameScopeList]
      if type(attributes) == type(""):
         attributes = [attributes]
      elif not attributes:
         attributes = ["all"]

      if attributes[0] == "all":
         attributes = self.attributes.keys()

      if not 'name' in attributes:
         attributes.append('name')
      if not 'scope' in attributes:
         attributes.append('scope')
      if not 'index' in attributes:
         attributes.append('index')
      response = []
      for nameScope in nameScopeList:
         try:
            (name, scope) = (nameScope['name'], nameScope['scope'])
         except:
            return {'results':{'concepts':[], 'statusCode':204}}

         res = self._getConceptByScopeWithValues((name,scope))
         if res[1] == 1:
            thisres = {}
            for attr in attributes:
               if res[0].has_key(attr):
                  thisres[attr] = res[0][attr]
            if thisres != {}:
               response.append(thisres)
         else:
            self.L._writeLog('fetchConcepts', ["FAIL", "f) getConceptByScopeWithValues returns failure"], [""], [], "", 2)
            return {'results':{'concepts':[], 'statusCode':200}}

      self.L._writeLog('fetchConcepts', ["  OK", "name: %s, scope: %s" % (name,scope)], [""], [], "", 2)
      return {'results':{'concepts':response,'statusCode':0}}


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   #
   # Here are some AgNIC-specific Public Methods.  
   # These are Public with user-level privledges, so in fact, are callable by any client. But, 
   # it's expected most clients will not find these useful.
   #


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('findPreferred')
   def findPreferred(self,  term=None, REQUEST=None):
      """ find the preferred term """

      global NOREQUEST, NOPREF, SUCCESS

      # a legacy method used by AgNIC
      if not term or not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ({}, NOREQUEST)

      if not self.A._allowed('browser', REQUEST['REMOTE_ADDR']):
         self.L._writeLog('findPreferred', ["FAIL", "invalid address"], [term], [], REQUEST['REMOTE_ADDR'], 2)
         return ({}, NOREQUEST)

      cname = canonical(term)

      if not self.concepts.has_key(cname):
         response = self._locateConcepts(cname, 1)  # level one searches only return one result
         if response[1] == 0:
            return ({}, NOPREF)

      res = self._getConceptByIndxWithValues(response[0][0])
      if res[1] == 0 or not res[0].has_key('use'):
         return ({}, NOPREF)

      return ({'name':term, 'use':res[0]['use']}, SUCCESS)



   #
   # end of the AgNIC-specific methods - - - - - - - - - - - - - - - - - - - - - - - - #


   #
   # Here are those public methods requiring "operator" access privledges
   #


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('info')
   def info(self, REQUEST=None):
      """ return some standard verbage about the service """

      global NOREQUEST, SUCCESS

      if not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ([], NOREQUEST)

      if not self.A._allowed('user', REQUEST['REMOTE_ADDR']):
         self.L._writeLog('info', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ([], NOACCESS)

      return (self._info(), SUCCESS)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('readSourceFile')
   def readSourceFile(self, sourcefile=None, sourcedir=None, thePath=None, REQUEST=None):
      """ read in a new thesaurus source file """

      global NOREQUEST, NOACCESS, READSOURCEFAIL, SUCCESS

      if not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ("", NOREQUEST)

      if not sourcefile and REQUEST.has_key('sourcefile'):
         sourcefile = REQUEST['sourcefile']
      else:
         sourcefile = self.theProperties['sourcefile']

      sourcedir = self.theProperties['sourcedir']
      thePath = self.theProperties['thePath']
      
      if not self.A._allowed('admin', REQUEST['REMOTE_ADDR']):
         self.L._writeLog('readSourceFile', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ("", NOACCESS)

      if not self._readThesaurusSource(sourcefile=sourcefile, sourcedir=sourcedir, thePath=thePath, REQUEST=REQUEST):
         self.L._writeLog('readSourceFile', ["FAIL", ''], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ("", READSOURCEFAIL)

      self.L._writeLog('readSourceFile', ["OK", ""], [], [], REQUEST['REMOTE_ADDR'], 2)
      return (sourcefile, SUCCESS)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('loadSource')
   def loadSource(self, sourcefile=None, schema=None, REQUEST=None):
      """ read in a new thesaurus source file """

      REQUEST.RESPONSE['loadStatus'] = "FAIL"

      if not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return self.manage_vocabulary(REQUEST)

      loaded=[]
      # we expect that this function is called from the ZMI and that a default name is
      # supplied for both sourcefile and schema. If either is null, indicating that
      # the user has deliberately cleared the form field, then we DO NOT load that file

      if not REQUEST.has_key('schema') or REQUEST['schema'] == "":
         pass
      else:
         if not schema and REQUEST.has_key('schema'):
            schema = REQUEST['schema']
   
         if not self.A._allowed('admin', REQUEST['REMOTE_ADDR']):
            self.L._writeLog('loadSource', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 2)
            return self.manage_vocabulary(REQUEST)
   
         if not self._readSchema(schema=schema):
            self.L._writeLog('loadSource', ["FAIL",""], [], [], REQUEST['REMOTE_ADDR'], 2)
            return self.manage_vocabulary(REQUEST)

         loaded.append("loaded schema: %s" % schema)
   
      if not REQUEST.has_key('sourcefile') or REQUEST['sourcefile'] == "":
         pass
      else:
         if not sourcefile and REQUEST.has_key('sourcefile'):
            sourcefile = REQUEST['sourcefile']
   
         if not self.A._allowed('admin', REQUEST['REMOTE_ADDR']):
            self.L._writeLog('loadSource', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 2)
            return self.manage_vocabulary(REQUEST)
   
         if not self._readThesaurusSource(sourcefile=sourcefile, REQUEST=REQUEST):
            self.L._writeLog('loadSource', ["FAIL",''], [], [], REQUEST['REMOTE_ADDR'], 2)
            return self.manage_vocabulary(REQUEST)
  
         loaded.append("loaded source: %s" % sourcefile)

      self.L._writeLog('loadSource', ["OK", str(loaded)], [], [], REQUEST['REMOTE_ADDR'], 2)
      REQUEST.RESPONSE['loadStatus'] = "SUCCESS"
      return self.manage_vocabulary(REQUEST)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('loggerConfig')
   def loggerConfig(self,  logfile=None, loglevel=None, REQUEST=None):
      """ loggerConfig called from ZMI """
  
      REQUEST.RESPONSE['loggerStatus'] = "FAIL" 
      if not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return self.manage_logger(REQUEST)
  
      self._refreshProperties() 

      if not logfile:
         if REQUEST.has_key('logfile'):
            logfile = REQUEST['logfile']
         else:
            logfile = self.theProperties['logfile']
      if not loglevel:
         if REQUEST.has_key('loglevel'):
            loglevel = REQUEST['loglevel']
         else:
            loglevel = self.theProperties['loglevel']

      if not self.A._allowed('admin', REQUEST['REMOTE_ADDR']):
         self.L._writeLog('loggerConfig', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return self.manage_logger(REQUEST)
   
      res = self.L._setlogging(logfilename=logfile, level=loglevel)
   
      self.L._writeLog('loggerConfig', ["OK", ""], [], [], REQUEST['REMOTE_ADDR'], 2)
      self._refreshProperties({'logfile':logfile, 'loglevel':loglevel})
      REQUEST.RESPONSE['loggerStatus'] = "SUCCESS" 
      return self.manage_logger(REQUEST)
   

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('wsdlConfig')
   def wsdlConfig(self, wsdlfile=None, REQUEST=None):
      """ wsdlConfig called from ZMI """

      self._refreshProperties()

      if not wsdlfile:
         wsdlfile = self.theProperties['wsdlfile']

      wsdlfilename = "%s/%s/%s" % (self.theProperties['thePath'], self.theProperties['configdir'], wsdlfile)
      self.wsdl = file(wsdlfilename).readlines()
      self._p_changed = 1

      return self.manage_wsdl(REQUEST)

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('accessConfig')
   def accessConfig(self,  hostsallowfile=None, consoles=None, REQUEST=None):
      """ accessConfig called from ZMI """
 
      REQUEST.RESPONSE['accessStatus'] = "FAIL" 
      if not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return self.manage_laccess(REQUEST)
   
      self._refreshProperties()

      if not hostsallowfile:
         if REQUEST.has_key('hostsallowfile'):
            hostsallowfile = REQUEST['hostsallowfile']
         else:
            hostsallowfile = self.theProperties['hostsallowfile']
      if not consoles:
         if REQUEST.has_key('consoles'):
            consoles = REQUEST['consoles']
         else:
            consoles = self.theProperties['consoles']

      if not self.A._allowed('admin', REQUEST['REMOTE_ADDR']):
         self._writeLog('accessConfig', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return self.manage_laccess(REQUEST)
   
      res = self.A._readHostsAllow()
   
      self.L._writeLog('accessConfig', ["OK", ""], [], [], REQUEST['REMOTE_ADDR'], 2)
      self._refreshProperties({'hostsallowfile':hostsallowfile, 'consoles':consoles})
      REQUEST.RESPONSE['accessStatus'] = "SUCCESS" 
      return self.manage_laccess(REQUEST)
   

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('loadOnCron')
   def loadOnCron(self, sourcefile=None, sourcedir=None, thePath=None, REQUEST=None):
      """ read in a new thesaurus source file """

      global NOSRCFOLDER, NOACCESS, SUCCESS, READSOURCEFAIL
      folderList = self.superValues('Folder')
      for fldr in folderList:
         if fldr.id == "Thesaurus":
            break
      else:
         self.L._writeLog('loadOnCron', ["FAIL",''], folderList, [], REQUEST['REMOTE_ADDR'], 2)
         return ("", NOSRCFOLDER)

      if not self.A._allowed('admin', REQUEST['REMOTE_ADDR']):
         self.L._writeLog('loadOnCron', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ("", NOACCESS)

      doLoad = fldr.getProperty('loadOnCron')
      if not doLoad:
         self.L._writeLog('loadOnCron', ["FAIL", "loadOnCron: NOT checked"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ("", SUCCESS)

      if not sourcefile and REQUEST.has_key('sourcefile'):
         sourcefile = REQUEST['sourcefile']

      if not sourcefile:
         fldr.getProperty('sourcefile')
      if not sourcedir:
         fldr.getProperty('sourcedir')
      if not thePath:
         fldr.getProperty('thePath')

      if not self._readThesaurusSource(sourcefile=sourcefile, sourcedir=sourcedir, thePath=thePath, REQUEST=REQUEST):
         self.L._writeLog('loadOnCron', ["FAIL",''], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ("", READSOURCEFAIL)

      self.L._writeLog('loadOnCron', ["OK", ""], [], [], REQUEST['REMOTE_ADDR'], 2)
      return (sourcefile, SUCCESS)



   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('echo')
   def echo(self, question=None, question2=None, REQUEST=None):
      """ echo a response """

      if not REQUEST and not question:
         return {'answer': "say what?"}

      answer="yada yada"
      if question:
         answer = "%s" % question
      if question2:
         answer = "%s, %s" % (answer, question2)

      # note - we don't do any IP checking for echo
      if hasattr(REQUEST, 'isSOAP'):   # soap invocation, find args in REQUEST object
         kw = getattr(REQUEST, 'kwargs')
         if kw.has_key('question'):
            question = kw['question']
         elif kw.has_key('question'):
            question = kw['question']
         if kw.has_key('question2'):
            question2 = kw['question2']

      return {'answer':'%s' % answer}
   

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

   """
   Here we begin the definition of functions that implement the REST protocol described by the
   Alexandria UCSB Thesaurus Protocol: www.alexandria.ucsb.edu/~gjanee/thesaurus/specification.html

   all public functions in this group have names that begine with ucsb_
   """
   
   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('get-properties')
   def ucsb_get_properties(self, REQUEST=None):
      """ return a standard description of this service """

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   # 
   # end of the Thesaurus class definition
   #
   # ------------------------------------------------------------------------------

# initialize the Thesaurus class
""" set up shop """
InitializeClass(ThesaurusFacility)
