# http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpclib
from xmlrpclib import ServerProxy

# Clicking on the 5 button on the image on the website brings up an XML
# file which is obviously an XML-RPC fault, see
# http://en.wikipedia.org/wiki/XML_RPC#Examples
# This leads us to believe that this level's URL is an XML-RPC service
# endpoint.

url = 'http://www.pythonchallenge.com/pc/phonebook.php'
serverProxy = ServerProxy(url)
methods = serverProxy.system.listMethods()

print 'Methods on server:'
print methods, '\n'

phoneNumber = serverProxy.phone('Bert')
print phoneNumber, '\n'

urlComponent = 'italy'
print 'urlComponent:'
print urlComponent
