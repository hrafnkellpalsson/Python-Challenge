# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image

oxygen = Image.open('oxygen.png')
# print 'format:', oxygen.format
# print 'size:', oxygen.size
print 'mode:', oxygen.mode
print ''

lineLength = 608
greyBox = (0, 43, lineLength, 52)
greyRegion = oxygen.crop(greyBox)
r, g, b, a = greyRegion.split()
greyData = list(greyRegion.getdata())
# The data from getData() if flattened out. Get only the first line
# since all the lines are the same anyway and therefore contain only
# redundant data.
greyLine = greyData[0:lineLength]

# The value of the a pixel is always 255 so it obviously contains no
# information. Let's strip it away.
rgbLine = [rgba[0:3] for rgba in greyLine]

# It seems that the values of the r, g and b pixels are always the same
# So it's just the single value of the r, g, b pixels that matters.
# Let's verify that the r, g, b values are always the same.
rgbIsSame = all([len(set(rgb)) == 1 for rgb in rgbLine])
if (not rgbIsSame):
    print 'The values of the r, g and b pixels are not always the same!'

# Now that we've verified that the value of r, g, b pixels is always the
# same let's extract that value.
numbers = [rgb[0] for rgb in rgbLine]

# It seems that each number in variable numbers occurs n*7
# times in a row where n is at least 1 (and is usually 1).
# So we guess that the number that repeats 7 times denotes one
# "unit of information".
# Note that for some reason the first number appears 5 times in a row
# and the last number appears 8 times in a row.
# Even though the first number appears 5 times and the last number
# appears 8 times we can get every number by extracting every seventh
# number from the nubmers variable starting at index 0.
numbersNoRepetition = [numbers[i] for i in range(0, lineLength, 7)]

# These numbers represent the ASCII code points for characters.
# Built-in function chr() give the character for a given code point
# and built-in functino ord() does the reverse.
# TODO Read http://www.joelonsoftware.com/articles/Unicode.html and then
# potentially modify this comment.
# Note that we could have used unichr() and ord(), that work for Unicode
# code points, since ASCII is a subset of Unicode.
ordinals = numbersNoRepetition
chars = [chr(ordinal) for ordinal in ordinals]
message = "".join(chars)
print message
print ''

ordinalsForUrl = [105, 110, 116, 101, 103, 114, 105, 116, 121]
charsForUrl = [chr(ordinal) for ordinal in ordinalsForUrl]
urlComponent = "".join(charsForUrl)

print 'url component:'
print urlComponent
