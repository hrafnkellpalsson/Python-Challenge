# http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image

cave = Image.open('cave.jpg')
mode = cave.mode
size = cave.size

data = list(cave.getdata())
dataOdd = data[1::2]
dataEven = data[0::2]

imageOdd = Image.new(mode, size)
imageOdd.putdata(dataOdd)
imageOdd.save('image_odd.jpg')

# Turns out the the latter image contains the same information as the
# first one so we don't need to show it.
# imageEven = Image.new(mode, size)
# imageEven.putdata(dataEven)
# imageEven.show()

urlComponent = 'evil'
print 'url component:'
print urlComponent
