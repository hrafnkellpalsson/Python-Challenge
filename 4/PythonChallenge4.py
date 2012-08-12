# http://www.pythonchallenge.com/pc/def/linkedlist.php
# Originally http://www.pythonchallenge.com/pc/def/linkedlist.html,
# which then just told us to change the ending from .html to .php

from urllib2 import Request, urlopen

# To hop in to the number sequence set number to 8022.
# To hop even further in to the number sequence set number to 37278.
number = 12345
number = 37278
numbers = [number]
messageBodyList = list()

while True:
    number = numbers[-1]
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%i' % (number,)
    request = Request(url=url)
    response = urlopen(request)
    messageBody = response.read()
    messageBodyList.append(messageBody)
    print "Message body: " + messageBody
    if "and the next nothing is" in messageBody:
        lastSepIndex = messageBody.rfind(" ")
        number = int(messageBody[lastSepIndex + 1:])
        numbers.append(number)
    elif "Yes. Divide by two and keep going." in messageBody:
        lastNumber = numbers[-1]
        print "%i/2 = %i" % (lastNumber, lastNumber / 2)
        numbers.append(lastNumber / 2)
    elif "There maybe misleading numbers in the text. One example is" in messageBody:
        lastSepIndex = messageBody.rfind(" ")
        number = int(messageBody[lastSepIndex + 1:])
        numbers.append(number)
    elif "peak.html" in messageBody:
        break
    else:
        "Error, unexpected message body from website."

urlComponent = messageBodyList[-1]
print "\nurlComponent: " + urlComponent
