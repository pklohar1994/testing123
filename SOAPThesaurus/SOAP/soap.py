"""SOAP support module

by Antonio Beamud Montero <antonio.beamud@linkend.com>

Based on the XML-RPC Zope support module written by Eric Kidd at UserLand 
software and the modifications made by Petru Paler, with much help 
from Jim Fulton at DC. 

This code hooks Zope up SOAPpy library.
"""

import sys
from string import replace
from HTTPResponse import HTTPResponse
#from SOAPpy import *
import SOAPpy
from zLOG import LOG, PROBLEM, ERROR, DEBUG, INFO,TRACE
from types import StringType

SOAPpy.Config.specialArgs=0.

def parse_input(data):
    """Parse input data and return a method path and argument tuple

    The data is a string.
    """

    obj = SOAPpy.parseSOAPRPC(data)
    method = obj._name
    args = tuple(obj._aslist())
  
    # Translate '.' to '/' in meth to represent object traversal.
    method = replace(method, '.', '/')
    return method, args, obj._asdict()

# See below
#
# def response(anHTTPResponse):
#     """Return a valid ZPublisher response object
# 
#     Use data already gathered by the existing response.
#     The new response will replace the existing response.
#     """
#     # As a first cut, lets just clone the response and
#     # put all of the logic in our refined response class below.
#     r=Response()
#     r.__dict__.update(anHTTPResponse.__dict__)
#     return r


      
    
#######################################################################
# New Object response based on SoapPy
#
class SOAPResponse:
    def __init__(self, real): self.__dict__['_real']=real
    def __getattr__(self, name): return getattr(self._real, name)
    def __setattr__(self, name, v): return setattr(self._real, name, v)
    def __delattr__(self, name): return delattr(self._real, name)

    def rmHigh(self, str):
        trlist = ''.join(map(chr, range(256)))
        dellist = ''.join(map(chr, range(128,256)))
        return str.translate(trlist, dellist)
    
    def setBody(self, body, method='', is_error=0, bogus_str_search=None):
        # Marshall our body as an SOAP response. Strings will be sent
        # strings, integers as integers, etc. We do *not* convert
        # everything to a string first.
        status = 200
        if isinstance(body, SOAPpy.faultType):
            # Convert Fault object to SOAP response.
            soapbody = SOAPpy.faulType("%s:Server" % SOAP.NS.ENV_T, self.rmHigh(body))                
            body = SOAPpy.buildSOAP(soapbody,encoding=None)
            status = 500
            #if type(body) == type(self) and isinstance(body, voidType):
            #    body = SOAPpy.buildSOAP(kw = {'%sResponse' % method: body})
        else:
            if type(body) is StringType:
                body = self.rmHigh(body)
            try:
#                body = SOAPpy.buildSOAP((body,),encoding=None)
                body = SOAPpy.buildSOAP(kw = {u'%sResponse' % method:body}, encoding=None)
            except Exception,e:
                self.SOAPexception()
                return 

        t = 'text/xml'

        self._real.setBody(body)
        self._real.setHeader('content-type', t)
        self._real.setHeader("content-length", str(len(body)))
        self._real.setStatus(status)
        return self

    def SOAPexception(self, fatal=0, info=None,
                      absuri_match=None, tag_search=None):
        # Fetch our exception info. t is type, v is value and tb is the
        # traceback object.

        if type(info) is type(()) and len(info)==3: t,v,tb = info
        else: t,v,tb = sys.exc_info()
        LOG('SOAPException',TRACE,tb)
        # Create an appropriate Fault object. Unfortunately, we throw away
        # most of the debugging information. More useful error reporting is
        # left as an exercise for the reader.
        Fault=SOAPpy.faultType
        f=None
        try:
            if isinstance(v, Fault):
                f=v
            elif isinstance(v, Exception):
                
                f=Fault("%s:Server" % SOAPpy.NS.ENV_T,
                        "Unexpected Zope exception: " + str(v))
            else:
                f=Fault("%s:Server" % SOAPpy.NS.ENV_T,
                        "Unexpected Zope error value: " + str(v))
        except:
            f=Fault("%s:Server" % SOAPpy.NS.ENV_T,
                    "Unknown Zope fault type")

        # Do the damage.
        body = SOAPpy.buildSOAP(f)
        self._real.setHeader('content-type', 'text/xml')
        self._real.setStatus(200)
        return tb

response=SOAPResponse
