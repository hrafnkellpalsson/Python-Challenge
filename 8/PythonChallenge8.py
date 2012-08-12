# http://www.pythonchallenge.com/pc/def/integrity.html

import bz2
from bz2 import decompress

# Information from the page's source:
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# When clicking the hidden link on the bee's wing we're asked for
# authentication. The pop-up says:
# A username and password are being requested by http://www.pythonchallenge.com. The site says: "inflate"
# By googling the first few letters of the variable un and pw we see
# that the letters denote a bz2 header.
username = decompress(un)
password = decompress(pw)

print "username: ", username
print "password: ", password

# Note that the area tag contained the missing parts of the new link the
# whole time!
urlComponent = "http://www.pythonchallenge.com/pc/return/good.html"
print "\nurl component:"
print urlComponent
