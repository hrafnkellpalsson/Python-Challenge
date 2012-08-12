# http://www.pythonchallenge.com/pc/def/peak.html

import pickle
from pprint import pprint

pickleFile = open('data.txt', 'rb')
data = pickle.load(pickleFile)

for d in data:
    print d

stringLines = []
for d in data:
    listLine = [charTuple[1] * charTuple[0] for charTuple in d]
    stringLine = "".join(listLine)
    stringLines.append(stringLine)

# Just as an exercise in list comprehensions, the for loop above can be
# condensed into this one-liner. But this is a rather unreadable line of
# code.
# stringLines = ["".join([charTuple[1] * charTuple[0] for charTuple in d]) for d in data]

for stringLine in stringLines:
    print stringLine
