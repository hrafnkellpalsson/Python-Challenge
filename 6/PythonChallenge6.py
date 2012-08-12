# http://www.pythonchallenge.com/pc/def/channel.html
# The zipper on the picture is a hint that we should download a zip file
# (the hint doensn't have anything to do with the zip() function!).
# The zip file is channel.zip, downloaded by visiting
# http://www.pythonchallenge.com/pc/def/channel.zip

from zipfile import ZipFile
from time import sleep

zipFileName = 'channel.zip'
zipFile = ZipFile(zipFileName, 'r')

zipNamelist = zipFile.namelist()
print 'LIST OF ARCHIVE MEMBERS:'
print zipNamelist

readmeFile = zipFile.open('readme.txt')
readmeText = readmeFile.read()
print '\nTEXT FROM readme.txt:'
print readmeText

memberTexts = []
number = 90052
numbers = [number]
memberComments = []

while True:
    number = numbers[-1]
    memberName = '%i.txt' % (number,)
    memberFile = zipFile.open(memberName)
    memberText = memberFile.read()
    memberTexts.append(memberText)

    memberInfo = zipFile.getinfo(memberName)
    memberComment = memberInfo.comment
    memberComments.append(memberComment)

    print number
    print memberTexts[-1]
    print memberComments[-1]
    print ''

    if "Next nothing is" in memberText:
        lastSepIndex = memberText.rfind(" ")
        number = int(memberText[lastSepIndex + 1:])
        numbers.append(number)
    elif "Collect the comments" in memberText:
        charSet = set(memberComments)
        break

# TODO Update this script to use the with statement
# http://docs.python.org/library/zipfile.html
# http://effbot.org/zone/python-with-statement.htm <-- Somewhat helpful, I might want to google more
zipFile.close()

# Rename memberComments to chars since now we know that the comments
# only include a single character.
chars = memberComments

# Find the order in which the characters appear.
charOrder = {chars.index(char): char for char in charSet}
charIndices = charOrder.keys()
charIndices.sort()
urlChars = [charOrder[index] for index in charIndices]
urlComponent = "".join(urlChars)

print 'url component:'
print urlComponent

# It seems that the stars, newlines and spaces in the member comments
# are there to try and trick us. Perhaps trick us into thinking that
# we are to try to make another ascii picture.
