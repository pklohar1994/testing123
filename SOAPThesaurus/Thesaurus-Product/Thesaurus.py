from Interface import Base

class Thesaurus(Base):
   """ create, populate, and manage a thesaurus """

   def verifyIP(self, ip, REQUEST=None):
      """ interface to Access Facility's verify IP """

   def addHostwithRole(self, host=None, role=None, REQUEST=None):
      """ interface to Access Facility's addHostwithRole """

   def deleteHostwithRole(self, host=None, role=None, REQUEST=None):
      """ interface to Access Facility's deleteHostwithRole """

   def getHostsAllow(self, REQUEST=None):
      """ interface to Access Facility's getHostsAllow """

   def myRole(self, REQUEST=None):
      """ interface to Access Facility's myRole """

   def readHostsAllow(self, REQUEST=None):
      """ interface to Access Facility's readHostsAllow """

   def reportLogStatus(self, REQUEST=None):
      """ interface to Logger Facility's reportLogStatus """

   def logMessage(self, who, msg, level=None, REQUEST=None):
      """ interface to Logger Facility's logMessage """

   def rotateLogFile(self, REQUEST=None):
      """ interface to Logger Facility's rotateLogFile """

   def setLogging(self, logfilename=None, level=None, REQUEST=None):
      """ interface to Logger Facility's setLogging """

   def setLogDefault(self, filename=None, REQUEST=None):
      """ interface to Logger Facility's setLogDefault """

   def tailLog(self, lines=10, REQUEST=None):
      """ interface to Logger Facility's tailLog method """

   def getTerm(self, expression, REQUEST=None):
      """ find the term that matches the expression """

   def findTerms(self, expression, REQUEST=None):
      """ find all terms that match expression """

   def searchForConcepts(self, termList=None, level=None, REQUEST=None):
      """ for each term in the list termList call _locateConcepts """

   def wsdl(self, REQUEST=None):
      """ wsdl returns the WSDL description file for these services """

   def fetchHier(self, nameScope=None, level=None, direction=None, REQUEST=None):
      """ fetch either the parents or children of indx to specified level """

   def hierFetch(self, nameScope=None, level=None, direction=None, REQUEST=None):
      """ fetch either the parents or children of indx to specified level """

   def fetchConcepts(self, nameScopeList=None, attributes=None, REQUEST=None):
      """ for each term in the list nameScopeList call _getConceptByScopeWithValues """

   def findPreferred(self,  term=None, REQUEST=None):
      """ find the preferred term """

   def info(self, REQUEST=None):
      """ return some standard verbage about the service """

   def readSourceFile(self, sourcefile=None, sourcedir=None, thePath=None, REQUEST=None):
      """ read in a new thesaurus source file """

   def loadSource(self, sourcefile=None, schema=None, REQUEST=None):
      """ read in a new thesaurus source file """

   def loggerConfig(self,  logfile=None, loglevel=None, REQUEST=None):
      """ loggerConfig called from ZMI """

   def wsdlConfig(self, wsdlfile=None, REQUEST=None):
      """ wsdlConfig called from ZMI """

   def accessConfig(self,  hostsallowfile=None, consoles=None, REQUEST=None):
      """ accessConfig called from ZMI """

   def loadOnCron(self, sourcefile=None, sourcedir=None, thePath=None, REQUEST=None):
      """ read in a new thesaurus source file """

   def echo(self, question=None, question2=None, REQUEST=None):
      """ echo a response """
