# http://www.pythonchallenge.com/pc/return/evil.html

# The file name evil1 leads us to suspect there might be another evil
# image. Right clicking the image in the browser and choosing 'View
# Image' we're taken to the url
# http://www.pythonchallenge.com/pc/return/evil1.jpg
# If we replace evil1.jpg in the url with evil2.jpg we are led to
# downloading evil2.gfx.
evil2 = open('evil2.gfx', 'r')
shuffledData = evil2.read()
evil2.close()

# Note, evil3.jpg and evil4.jpg also exist. evil4.jpg actually just
# seems to be a text file. Chrome and Firefox weren't able to show the
# contents of the text file, probably because they were fixating on the
# file ending. Internet Explorer could open the text file which read:
# "Bert is evil! go back!"
# Using wget --user huge --password file http://www.pythonchallenge.com/pc/return/evil4.jpg
# worked and the file command identified it as ASCII text.
# We will need to keep this piece information in mind for level 13.

# .gfx is some obscure file format, so we use a hex editor to view the
# file. Can't find any information on the header of the file on Google,
# which could be considered normal since .gfx is an obscure format.
# However, if hex codes for headers had been a special interest of ours,
# we might have noticed that the JPG, PNG and GIF87a headers occur with
# where every fifth byte belongs to the same header.
unshuffledData = [shuffledData[i::5] for i in xrange(5)]

# Using Gary Kessler's list of file signatures,
# http://www.garykessler.net/library/file_sigs.html, we identify the
# headers. We need the bytearray cast and built-in hex function to see
# the hex values.
# Note that this code is not needed to solve the problem.
headers = ['JPG', 'PNG', 'GIF87a', 'PNG', 'JPG']
print 'Headers:'
for i in xrange(5):
    print [hex(entry) for entry in bytearray(unshuffledData[i][0:5])], ' - ', headers[i]

# Note that we never needed to use the PIL library in this problem!
[open("unshuffled_%d.dat" % i, "w").write(unshuffledData[i]) for i in xrange(5)]

urlComponent = 'disproportionality'
print '\nurl component:'
print urlComponent
