#!/usr/bin/python

# A demonstration of why "truth of x==y does not imply falsehood of x!=y" due
# to Python effectively implementing == as an alias to __eq__ and != as an 
# alias to __ne__

import sys

# This class implements its own __eq__ and __ne__ methods in a stupid way.
class StupidInt:
    def __init__(self, val):
        self.value = val

    def __eq__(self, compare):
        return self.value == 3

    def __ne__(self, compare):
        return self.value != 5


def main():
    value1 = StupidInt(3)
    value2 = StupidInt(5)

    print "value1 : {0}".format(value1.value)
    print "value2 : {0}".format(value2.value)
    print "value1 == value2 : {0}".format(value1 == value2)
    print "value2 == value1 : {0}".format(value2 == value1)
    print "value1 != value2 : {0}".format(value1 != value2)
    print "value2 != value1 : {0}".format(value2 != value1)
    sys.exit(0)

if __name__ == '__main__':
    main()