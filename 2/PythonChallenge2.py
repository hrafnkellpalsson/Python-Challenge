# http://www.pythonchallenge.com/pc/def/ocr.html

import string

dataFile = open('data.txt', 'r')
mess = dataFile.read()

# Find the rare characters.
messSet = set(mess)
charFrequency = {char: mess.count(char) for char in messSet}
rareChars = [char for (char, frequency) in charFrequency.iteritems() if frequency == 1]

# Find the order in which the characters appear.
charOrder = {mess.index(char): char for char in rareChars}
charIndices = charOrder.keys()
charIndices.sort()
urlChars = [charOrder[index] for index in charIndices]
urlComponent = "".join(urlChars)

print 'url component:'
print urlComponent
