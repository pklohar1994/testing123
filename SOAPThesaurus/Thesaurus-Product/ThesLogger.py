from Logger import Logger
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
NOREQUEST  = 201       # no REQUEST object seen
NOACCESS   = 202       # access not allowed

# access codes
NOROLE     = 231       # no role specified
SAVEHOSTSFAIL = 232    # failure to re-save/re-write hosts file
DELROLEFAIL   = 233    # failure to delete role for host
LOADHOSTSFAIL = 234    # failure to load hosts.allow

# logger codes
WRITEFAIL  = 221       # fail to write to log file
SETLOGFAIL = 223       # failure to set/reset log
GETLOGFAIL = 224       # failure to get logging info
INVLEVEL   = 226       # invalid log level specified
ROTFAIL    = 227       # failure to rotate logfile


logfd = None

def addLogger(dispatcher, id, REQUEST=None):
   """ add the logger sub-system facility for the Thesaurus product """
   L = LoggerFacility(id)
   dispatcher.Destination()._setObject(id, L)


################################################################################################
################################################################################################

class LoggerFacility(Implicit, Persistent, RoleManager, Item):
   """ instantiate the logging facility """

   __implements__ = Logger

   meta_type = 'Logger'

   manage_options = (
      {'label' : 'Edit',
       'action' : 'initLogger',
       'help'   : ('Thesaurus', 'help.txt')
       },
      {'label'  : 'View',
       'action' : 'administer',
       'help'   : ('Thesaurus', 'help.txt')
       },
      ) + RoleManager.manage_options + Item.manage_options

   security = ClassSecurityInfo()

   security.declarePublic('View management screens')
   initLogger = PageTemplateFile('www/initLogger', globals())

   security.declarePublic('administer')
   administer = PageTemplateFile('www/administer', globals())


   def __init__(self, id):
      """ instantiate the logger service """
      self.id = id
      self.loglevel = None
      self.logfile = None
      self.logdefault = None
      self.consoles = None
      self.Access = None
      self.T = None
      self.theProperties = {}

   # consoles is a list of IPs that are considered 'safe' to access functions here
   # if Access has not been instantiated.  Look at the calls to self.Access._allowed below.
   # If the call to self.R._allowed fails, we still grant access if connection is
   # from one of the designated consoles.

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_initLogger')
   def _initLogger(self, T):
      """ initialize the logger facility """

      global logfd

      self.T = T
      self.theProperties = self.T._refreshProperties()
      thePath = self.T.theProperties['thePath']
      logsdir = self.T.theProperties['logsdir']
      logfile = self.T.theProperties['logfile']
      self.logdefault = self.T.theProperties['defaultLogFile']
      if not logfile:
         logfile = self.logdefault

      self.logfile = "%s/%s/%s" % (thePath, logsdir, logfile)

      self.loglevel = self.T.theProperties['loglevel']
      if self.loglevel > 0:
         logfd = open(self.logfile, 'w')

      self.consoles = self.T.theProperties['consoles']
      self._p_changed = 1

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_setAccessRef')
   def _setAccessRef(self, accessFacility):
      """ set a refernce to the Access machinery """
      self.Access = accessFacility
      self._p_changed = 1

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_tail')
   def _tail(self, num):
      """ get the last num of lines from the log file """

      if not num:
         num = 10

      num = int(num)
      if num > 100:
         num = 100

      try:
         fd = open(self.logfile, 'r')
      except:
         return []

      lines = []
      looped = 0
      for n in range(num):
         lines.append('')
      n = -1
      try:
         while n < num:
            line = fd.readline()
            if not line:
               fd.close()
               if looped == 0 and n < num:
                  num = n + 1
               break
            n += 1
            if n >= num:
               n = 0
               looped = 1
            lines[n] = line.strip()
      except:
         fd.close()

      b = 0
      e = n
      if looped:
         b = n + 1
         if b == num:
            b = 0
         for i in range(0,b):
            lines.append(lines[i])

      e = b + num
      return lines[b:e]


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_writeLog')
   def _writeLog(self, func, disp, termList, attrList, client, level):
      """ write a line to the log file recording clientIP, date/time,  method and method args """

      global logfd

      if self.loglevel == 0:
         return 0

      if level > self.loglevel:
         return 0

      terms=""
      theDate = time.ctime()
      if termList:
         terms = str(termList)

      attrs=""
      if attrList:
         attrs = str(attrList)

      if len(disp) == 1:
         disp.append("")

      try:
         logfd.write("%s : %s : %s : %4.4s : %s : %s : %s : %d\n" % (client, theDate, func, disp[0], disp[1], terms, attrs, level))
         logfd.flush()
         return 1
      except:   # loglevel is > 0, so let's try re-opening the logfile
         try:
            self._setlogging(level=self.loglevel)
            logfd.write("%s : %s : %s : %4.4s : %s : %s : %s : %d\n" % (client, theDate, func, disp[0], disp[1], terms, attrs, level))
            logfd.flush()
            return 1
         except:
            return 0

      # should never get here
      return 0


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_rotateLog')
   def _rotateLog(self, newLog=None):
      """ rotate the log file using new logfile name if supplied """

      # the Public method "rotateLog" does not provide supplying a filename as an option
      #   rotateLog is provided as an 'operator' method that simply allows logs to be rotated
      #   without changing the filename

      global logfd

      self.theProperties = self.T._refreshProperties()
      self.thePath = self.theProperties['thePath']
      self.logsdir = self.theProperties['logsdir']
      self.logfile = self.theProperties['logfile']
      self.loglevel = int(self.theProperties['loglevel'])

      # called without a filename, close current file and open logfile
      if not newLog:
         newLog = self.logfile

      # regardless, chop off any path
      newLog = os.path.basename(newLog)

      newLogPath = "%s/%s/%s" % (self.thePath, self.logsdir, newLog)

      theDate = time.ctime()

      logfd.close()

      # have to now rename the old file in case we're re-using the filename
      # now rename current file to something useful and unique
      suffix = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())

      logfilepath = "%s/%s/%s" % (self.thePath, self.logsdir, self.logfile) 
      cmd = "mv %s %s.%s" % (logfilepath, logfilepath, suffix)
      if os.system(cmd) != 0:   # zero returned is success
         mvmsg = "cannot %s" % cmd
         oldlogfile = ""
      else:
         mvmsg = "renamed old logfile %s to %s.%s" % (logfilepath, logfilepath, suffix)
         oldlogfile = "%s.%s" % (self.logfile, suffix)

      if self.loglevel != 0: 
         newLog = "%s/%s/%s" % (self.thePath, self.logsdir, newLog)

         try:
            logfd = open(newLogPath, 'a')
            self.logfile = newLogPath
            msg = "%s opened" % newLogPath
         except:              # too bad the log file isn't available to log this failure :)
            self.loglevel = 0
            return ["", -1]  # will return -1 to differentiate from normally closed log level

      return [oldlogfile, self.loglevel]

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePrivate('_setlogging')
   def _setlogging(self, logfilename=None, level=None):
      """ set logging to indicated level """

      #  0 : off, no logging
      #  1 : normal, just log the web service traffic
      #  2 : daemon, log all messages from the daemon process and all #1 stuff
      #  3 : debug,  log everything

      # we are careful here not to call writeLog as it calls setlogging

      global logfd

      theDate = time.ctime()
      self.theProperties = self.T._refreshProperties()
      self.thePath = self.theProperties['thePath']
      self.logsdir = self.theProperties['logsdir']
      self.logfile = "%s/%s/%s" % (self.thePath, self.logsdir, self.theProperties['logfile'])
      if level:
         level = int(level)
      else:
         level = self.theProperties['loglevel']

      if not logfilename:
         logfilename = self.logfile
      else:
         if logfilename[-4:] != '.log':
            logfilename = "%s.log" % logfilename
         logfilename = os.path.basename(logfilename)
         logfilename = "%s/%s/%s" % (self.thePath, self.logsdir, logfilename)

      if logfilename != self.logfile:
         res = self._rotateLog(newLog=logfilename)

      # bogus level
      if level < 0 and 3 < level:
         if self.loglevel > 0:
            try:
               logfd.write("%s : %s : %s : %s : : %d\n" % ("daemon", theDate, '_setlogging', ("bogus level: %d" % level), 3))
               logfd.flush()
            except:
               logfd.close()
               self.loglevel = 0

      # turn off logging
      if level == 0:
         if self.loglevel == 0:
            return [self.logfile, self.loglevel]
         else:
            try:
               logfd.write("%s : %s : %s : %s : : %d\n" % ("daemon", theDate, '_setlogging', "set logging to 0", 3))
               logfd.flush()
               logfd.close()
            except:
               pass

         self.loglevel = 0

      # turn on logging or change level
      if level > 0:
         try:
            logfd = open(logfilename, 'a')
            self.logfile = logfilename
            self.loglevel = level
         except:
            self.loglevel = 0

      self.manage_changeProperties({'loglevel':level})
      self._p_changed = 1
      return [self.logfile, self.loglevel]


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('tailLOg')
   def tailLog(self, lines=None, REQUEST=None):
      """ report on whether we are logging to a file """

      global NOREQUEST, NOACCESS, GETLOGFAIL, SUCCESS

      if not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ([], NOREQUEST)

      try:
         lines = str(int(lines))
      except:
         lines = "10"

      if not self.Access._allowed('operator', REQUEST['REMOTE_ADDR']):
         self._writeLog('tailLog', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 1)
         return ([], NOACCESS)

      lines = self._tail(lines)
      if lines == []:
         return ([], GETLOGFAIL)

      self._writeLog('tailLog', ["OK", ""], [], [], REQUEST['REMOTE_ADDR'], 1)
      return (lines, SUCCESS)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('reportLogStatus')
   def reportLogStatus(self, REQUEST=None):
      """ report on whether we are logging to a file """

      global NOREQUEST, NOACCESS, SUCCESS

      if not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ([], NOREQUEST)

      if not self.Access._allowed('operator', REQUEST['REMOTE_ADDR']):
         self._writeLog('reportLogStatus', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 1)
         return ([], NOACCESS)

      self._writeLog('reportLogStatus', ["OK", ''], [], [], REQUEST['REMOTE_ADDR'], 1)
      return ([self.logfile, self.loglevel], SUCCESS)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('logMessage')
   def logMessage(self, who, msg, level=None, REQUEST=None):
      """ write a message to the log file """

      global NOREQUEST, NOACCESS, INVLEVEL, SUCCESS

      if not level or not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ("FAIL", NOREQUEST)

      if not self.Access._allowed('operator', REQUEST['REMOTE_ADDR']):
         self._writeLog('logMessage', ["FAIL", "invalid address"], [who, msg], [], REQUEST['REMOTE_ADDR'], 1)
         return ("FAIL", NOACCESS)

      try:
         level = int(level)
      except:
         self._writeLog('logMessage', ["FAIL", "illegal value/type for level"], [who, msg], [], REQUEST['REMOTE_ADDR'], 1)
         return ("FAIL", INVLEVEL)

      if level < 0 or 3 < level:
         self._writeLog('logMessage', ["FAIL", "invalid level: %s" % level], [who, msg], [], REQUEST['REMOTE_ADDR'], 1)
         return ("FAIL", INVLEVEL)

      try:
         self._writeLog('logMessage', ["", who], [msg], [], REQUEST['REMOTE_ADDR'], 1)
         return (msg, SUCCESS)
      except:
         pass
      return ("FAIL", WRITEFAIL)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('rotateLogFile')
   def rotateLogFile(self, REQUEST=None):
      """ rotate the log file """

      global NOREQUEST, NOACCESS, ROTFAIL, SUCCESS

      if not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ([], NOREQUEST)

      if not self.Access._allowed('operator', REQUEST['REMOTE_ADDR']):
         self._writeLog('rotateLogFile', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 1)
         return ([], NOACCESS)

      (archivefile, level) = self._rotateLog()
      # level holds current loglevel or -1 indicating failure to re-open file
      # archivefile holds archived filename or "" if we could not 'mv' the logfile to archive name format

      self._writeLog('rotateLogFile', ["OK", ''], [], [], REQUEST['REMOTE_ADDR'], 1)
      if res[1] == -1:
			return([archivefile, level], ROTFAIL)
      return ([archivefile, level], SUCCESS)


   # here are the methods requiring "admin" privledges
   #

   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('setLogging')
   def setLogging(self,  logfilename=None, level=None, REQUEST=None):
      """ setLogging on or off """

      global NOREQUEST, NOACCESS, SETLOGFAIL, SUCCESS

      if not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ([], NOREQUEST)

      if not logfilename:
         logfilename = self.logfile

      # don't do anything, but return success nevertheless
      if level == self.loglevel and logfilename == self.logfile:
         self._writeLog('setLogging', ["OK", ''], [], [], REQUEST['REMOTE_ADDR'], 1)
         return ([self.logfile, self.loglevel], SUCCESS)

      level = int(level)

      self._writeLog('setLogging', ["OK", "set log file attempt: %s with level %s" % (logfilename, level)], [], [], REQUEST['REMOTE_ADDR'], 1)
      if not self.Access._allowed('admin', REQUEST['REMOTE_ADDR']):
         self._writeLog('setLogging', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 1)
         return ([], NOACCESS)

      [newfile, newlevel] = self._setlogging(logfilename=logfilename, level=level)
      if ( (newfile == logfilename) and (newlevel == level) ):
         return ([self.logfilename, self.loglevel], SUCCESS)
      else: 
         return ([self.logfilename, self.loglevel], SETLOGFAIL)


   #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
   security.declarePublic('setLogDefault')
   def setLogDefault(self, newdefault=None, REQUEST=None):
      """ reset the default logfile name """

      global NOREQUEST, NOACCESS, SUCCESS

      if not newdefault or not REQUEST or not REQUEST.has_key('REMOTE_ADDR'):
         return ([], NOREQUEST)

      if not self.Access._allowed('admin', REQUEST['REMOTE_ADDR']):
         self._writeLog('setLogDefault', ["FAIL", "invalid address"], [], [], REQUEST['REMOTE_ADDR'], 1)
         return ([], NOACCESS)

      # Note: this doesn't actually change the current logfile output.
      # To actually change the output, call _rotateLog

      # hmmm, this should really have a private analog to do the work and set _p_changed
      self.logdefault = newdefault
      self._p_changed = 1

      self._writeLog('setLogDefault', ["OK", ''], [], [], "", 1)
      return ([self.logdefault,self.loglevel], SUCCESS)


InitializeClass(LoggerFacility)
