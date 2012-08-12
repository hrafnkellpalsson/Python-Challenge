# http://www.pythonchallenge.com/pc/return/bull.html

from numpy import array

# This is the sequence http://en.wikipedia.org/wiki/Look-and-say_sequence
# a = [1, 11, 21, 1211, 111221,

# From the article:
# No digits other than 1, 2, and 3 appear in the sequence, unless the
# seed number contains such a digit or a run of more than three of the
# same digit.
# So we only need to worry about the digits 1, 2 and 3 and we know
# that none of them can appear more than three times in a row.


def nextLookAndSayTerm(term):
    # We need a string for the algorithm we've implemented.
    term = str(term)

    pairs = []
    # Give previousDigit a nonsensical value so we can go trough the
    # first digit == previousDigit comparison.
    previousDigit = -1
    # The constrained range since no digit can occur more than three
    # times in a row.
    constrainedRange = array(range(1, 3))

    for i, digit in enumerate(term):
        if digit == previousDigit:
            continue
        previousDigit = digit

        seekRange = i + constrainedRange
        seekRange = [index for index in seekRange if index < len(term)]
        numOccurences = 1

        # This 'if' covers the case when the last digit of a term is
        # only the last digit, not the penultimate digit as well.
        if seekRange == []:
            pair = '1' + digit
            pairs.append(pair)

        # This is the 'main logic' of the algorithm.
        for index in seekRange:
            if term[index] == digit:
                numOccurences += 1
            else:
                pair = str(numOccurences) + digit
                pairs.append(pair)
                break

            # This 'if' covers the case when the last digit of a term is
            # also the penultimate digit.
            # This 'if' is also needed if the same digit appears three
            # times in a row in the term.
            if index == seekRange[-1]:
                pair = str(numOccurences) + digit
                pairs.append(pair)

    nextTerm = int(''.join(pairs))
    return nextTerm

a = [1, 11, 21, 1211, 111221]
term = a[-1]
for i in xrange(26):
    nextTerm = nextLookAndSayTerm(term)
    a.append(nextTerm)
    term = nextTerm

# len function doesn't work on Integer or Long so we convert to String.
urlComponent = len(str(a[30]))

print 'urlComponent:'
print urlComponent
