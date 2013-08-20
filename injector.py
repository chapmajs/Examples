#!/usr/bin/python

# Demonstrating dependency injection on a module in Python. We import our
# module, `injectable.py`, and call a few methods on it. The dependency
# that is passed in is stored locally in the module and is called by methods
# local to the module.

import sys
import injectable

# We're going to inject this method, since methods are first-class objects
def test():
  print "The test method was invoked!"

def main():
  injectable.injectDependency(test)
  injectable.printDependency()
  injectable.callDependency()
  sys.exit(0)

if __name__ == "__main__":
  main()
