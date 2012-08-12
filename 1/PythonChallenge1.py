# http://www.pythonchallenge.com/pc/def/map.html
# Originally http://www.pythonchallenge.com/pc/def/274877906944.html
# which just redirected to the first url.

import string
from string import maketrans

data = open('data.txt', 'r')
text = data.read()
data.close()

asciiLowercaseTranslated = "cdefghijklmnopqrstuvwxyzab"

transTable = maketrans(string.ascii_lowercase, asciiLowercaseTranslated)
translatedText = text.translate(transTable)
print translatedText

urlComponent = "map".translate(transTable)
print "url component:"
print urlComponent
