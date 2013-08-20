#!/usr/bin/python

# Demonstrate dependency injection in Python 2. After including this module, 
# set the dependency with injectDependency(). It can then be accessed via
# getDependency(). callDependency() will treat the injected dependency as a 
# method and call it.

def injectDependency(dep):
  global __YOURDEP__
  __YOURDEP__ = dep

def getDependency():
  return __YOURDEP__

def printDependency():
  print __YOURDEP__

def callDependency():
  __YOURDEP__()
