from Access import Access
from AccessControl import ClassSecurityInfo, getSecurityManager
from Globals import InitializeClass, DTMLFile, package_home
from Acquisition import Implicit
from Globals import Persistent
from AccessControl.Role import RoleManager
from OFS.SimpleItem import Item
from Products.PageTemplates.PageTemplateFile import PageTemplateFile

import sys, os
import string
import pickle
import re
import xmlrpclib
import types
import time


# general codes
SUCCESS    =   0
NOREQUEST  = 201
NOACCESS   = 202

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

def addFunction(dispatcher, id, REQUEST=None):
   """ instantiate the access facility for thesaurus web service """
   R = AccessFacility(id)
   dispatcher.Destination()._setObject(id, R)



################################################################################################
################################################################################################

class AccessFacility(Implicit, Persistent, RoleManager, Item):
   """ create the roles facility for managing access to the service """

   __implements__ = Access

   meta_type = 'AccessFacility'

   manage_options = (
      {'label' : 'Edit',
       'action' : 'initAccess',
       'help'   : ('Thesaurus', 'accesshelp.txt')
       },
      {'label'  : 'View',
       'action' : 'adminAccess',
       'help'   : ('Thesaurus', 'accesshelp.txt')
       },
      ) + RoleManager.manage_options + Item.manage_options

   security = ClassSecurityInfo()

   security.declarePublic('View management screens')
   initAccess = PageTemplateFile('www/initAccess', globals())

   security.declarePublic('administer')
   adminAccess = PageTemplateFile('www/adminAccess', globals())


   def __init__(self, id):
      """ instantiate the roles service """
      self.id = id
      self.roles = {}
      self.Logger = None # the logger
      self.hostsallowfile = None
      self.consoles = []
      self.theProperties = {}
      self.T = None


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_initAccess')
   def _initAccess(self, T):
      """ initial the facility and read the config file """
      self.T = T
      self.theProperties = self.T._refreshProperties()
      thePath = self.theProperties['thePath']
      configdir = self.theProperties['configdir']
      hostsallowfile = self.theProperties['hostsallowfile']

      self.hostsallowfile = "%s/%s/%s" % (thePath, configdir, hostsallowfile)
      self.consoles = self.theProperties['consoles']
      self._p_changed = 1

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_setLoggerRef')
   def _setLoggerRef(self, logger):
      """ get a reference to the logger facility """
      self.Logger = logger
      self._p_changed = 1

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_readHostsAllow')
   def _readHostsAllow(self):
      """ read the IP control file for valid web services connections """

      self.Logger._writeLog('_readHostsAllow', ["OK","file: %s" % self.hostsallowfile], [],[], "daemon", 3)

      self.roles['user'] = {}
      self.roles['operator'] = {}
      self.roles['admin'] = {}
      # we add the console IPs regardless of what's in the hosts.allow file
      self.theProperties = self.T._refreshProperties()
      self.consoles = self.theProperties['consoles']
      self.hostsallowfile = "%s/%s/%s" % (self.theProperties['thePath'], self.theProperties['configdir'], self.theProperties['hostsallowfile'])

      try:
         lines = file(self.hostsallowfile).readlines()
      except:
         self.Logger._writeLog('_readHostsAllow', ["FAIL","cannot read hostsAllow file: %s" % self.hostsallowfile], [], [],"daemon", 3)
         return ""

      role = ""
      for line in lines:
         if line[0] in '\n#':
            continue
         if line[0] in '\t ':
            if not role:
               continue
            IPList = line.strip()
         else:
            line = line.strip()
            (role, IPList) = line.split(':', 1)
            if not role in ['user', 'operator', 'admin']:
               continue
         IPs = IPList.split(',')
         iplist = []
         for ip in IPs:
            ip = ip.strip()
            if len(ip) > 0:
               self.roles[role][ip] = 1

      self.Logger._writeLog('_readHostsAllow', ["OK", ''], [], [], "daemon", 3)
      self._p_changed = 1
      return self.hostsallowfile


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_writeHostsAllow')
   def _writeHostsAllow(self):
      """ write out a new hosts file """

      self.Logger._writeLog('_writeHostsAllow', ["OK", "attempt to write a new hosts.allow file"], [], [], "daemon", 1)
      self.theProperties = self.T._refreshProperties()
      self.hostsallowfile = "%s/%s/%s" % (self.theProperties['thePath'], self.theProperties['configdir'], self.theProperties['hostsallowfile'])
      newhosts = self.hostsallowfile + ".new"
      try:
         lines = file(self.hostsallowfile).readlines()
         fo = open(newhosts, 'w')
      except:
         self.Logger._writeLog('_writeHostsAllow', ["FAIL", '1'], [],[], "daemon", 3)
         return 0

      for line in lines:
         if line[0] == '#' or line[0] == '\n':
            fo.write(line)
            continue
         break

      linepack = 5
      for role in ['user', 'operator', 'admin']:
         if self.roles.has_key(role):
            n = 0
            newline = "%s:" % role
            for ip in self.roles[role].keys():
               newline = "%s %s," % (newline,ip)
               n = n + 1
               if n > linepack:
                  fo.write("%s\n" % newline)
                  newline = "%s:" % role
                  n = 0
            if n > 0:
               fo.write("%s\n" % newline)
         
      try:
         os.system("mv %s %s" % (newhosts, self.hostsallowfile))
         self.Logger._writeLog('_writeHostsAllow', ["OK",''], [], [], "daemon", 3)
         return 1
      except:
         self.Logger._writeLog('_writeHostsAllow', ["FAIL", '2'], [], [], "daemon", 3)
         return 0


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_allowed')
   def _allowed(self, role, IP):
      """ indicate if IP has role """

      if role == 'browser':
         return 1

      if IP in self.consoles:
         return 1

      if IP in self.roles['admin'].keys():
         return 1

      if IP in self.roles['operator'].keys():
         if role == 'user' or role == 'operator':
            return 1

      if IP in self.roles['user'].keys():
         if role == 'user':
            self.Logger._writeLog('_allowed', ["OK", "%s/%s" % (IP, role)], [] , [], "daemon", 3)
            return 1

      self.Logger._writeLog('_allowed', ["FAIL", "invalid IP/role %s/%s" % (IP, role)], [], [], "daemon", 3)
      return 0

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_getHostsAllow')
   def _getHostsAllow(self):
      """ return a dict of the current in-memory hosts config """

      return self.roles

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_myRole')
   def _myRole(self, REQUEST=None):
      """ return role for the given IP """

      IP = REQUEST['REMOTE_ADDR']

      for role in ['admin', 'operator', 'user']:
         if IP in self.roles[role].keys():
            return role
         
      return IP


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('verifyIP')
   def verifyIP(self, ip, REQUEST=None):
      """ indicate what role the ip has """

      if not ip or not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ("", NOREQUEST)

      if not self._allowed('operator', REQUEST['REMOTE_ADDR']):
         self.Logger._writeLog('verifyIP', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ("", NOACCESS)

      roles = ['operator', 'user']

      if self._myRole(REQUEST) == 'admin':
         roles = ['admin', 'operator', 'user']

      # check in this order: admin, operator, user
      for role in roles:
         if ip in self.roles[role].keys():
            self.Logger._writeLog('verifyIP', ["OK", "%s/%s" % (ip, role)], [], [], REQUEST['REMOTE_ADDR'], 2)
            return (role, SUCCESS)

      self.Logger._writeLog('verifyIP', ["%s/%s" % (ip, "NO ROLE")], [], [], REQUEST['REMOTE_ADDR'], 2)
      return ("", NOROLE)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('addHostwithRole')
   def addHostwithRole(self, host=None, role=None, REQUEST=None):
      """ add a host with role to hostsallow file and make it active """

      if not host or not role or not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ([], NOREQUEST)

      if not self._allowed('admin', REQUEST['REMOTE_ADDR']):
         self.Logger._writeLog('addHostwithRole', ["FAIL", "invalid address: host: %s, role: %s" % (host, role)], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ([], NOACCESS)

      if not role in ['user', 'operator', 'admin']:
         return ([], NOROLE)

      self.roles[role][host] = 1

      if not self._writeHostsAllow():
         del self.roles[role][host]
         self.Logger._writeLog('addHostwithRole', ["FAIL", ''], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ([], SAVEHOSTSFAIL)

      self.Logger._writeLog('addHostwithRole', ["OK", ''], [], [], REQUEST['REMOTE_ADDR'], 2)
      self._p_changed = 1
      return ([host, role], SUCCESS)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('deleteHostwithRole')
   def deleteHostwithRole(self, host=None, role=None, REQUEST=None):
      """ delete a host with role in the hostsallow file and make change active """

      if not host or not role or not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ([], NOREQUEST)

      if not self._allowed('admin', REQUEST['REMOTE_ADDR']):
         self.Logger._writeLog('deleteHostwithRole', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ([], NOACCESS)

      if not role in ['user', 'operator', 'admin']:
         self.Logger._writeLog('deleteHostwithRole', ["FAIL", "invalid role"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ([], NOROLE)

      try:
         del self.roles[role][host]
      except:
         self.Logger._writeLog('deleteHostwithRole', ["FAIL", "invalid host"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ([], DELROLEFAIL)

      if not self._writeHostsAllow():
         self.roles[role][host] = 1
         self.Logger._writeLog('deleteHostwithRole', ["FAIL", ''], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ([], SAVEHOSTSFAIL)

      self.Logger._writeLog('deleteHostwithRole', ["OK", ''], [], [], REQUEST['REMOTE_ADDR'], 2)
      self._p_changed = 1

      return ([host,role], SUCCESS)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('getHostsAllow')
   def getHostsAllow(self, REQUEST=None):
      """ return the in-memory hosts.allow configuration """

      if not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ( {}, NOREQUEST)

      if not self._allowed('admin', REQUEST['REMOTE_ADDR']):
         self.Logger._writeLog('getHostsAllow', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ( {}, NOACCESS)

      self.Logger._writeLog('getHostsAllow', ["OK", ''], [], [], REQUEST['REMOTE_ADDR'], 2)
      return (self._getHostsAllow(), SUCCESS)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('myRole')
   def myRole(self, REQUEST=None):
      """ return my role as specified by my IP and hosts allow """

      if not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         self.Logger._writeLog('myRole', ["FAIL", "invalid address"], [], [], "", 2)
         return ("", NOREQUEST)

      if not self._allowed('user', REQUEST['REMOTE_ADDR']):
         self.Logger._writeLog('myRole', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ("", NOACCESS)

      self.Logger._writeLog('myRole', ["OK", ''], [], [], REQUEST['REMOTE_ADDR'], 3)
      return (self._myRole(REQUEST), SUCCESS)



   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('readHostsAllow')
   def readHostsAllow(self, REQUEST=None):
      """ read or re-read the hosts.allow file """

      if not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ("", NOREQUEST)

      if not self._allowed('admin', REQUEST['REMOTE_ADDR']):
         self.Logger._writeLog('readHostsAllow', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 2)
         return ("", NOACCESS)

      self.Logger._writeLog('readHostsAllow', ["OK", ''], [], [], REQUEST['REMOTE_ADDR'], 2)
      res = self._readHostsAllow()
      if res != "":
         return (self._readHostsAllow(), SUCCESS)
      else:
         return ("", LOADHOSTSFAIL)

InitializeClass(AccessFacility)
