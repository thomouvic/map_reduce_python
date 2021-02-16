#!/usr/bin/env python
"""mapper.py"""

def emit(key, value):
  print('%s\t%s' % (key, value))

def mapper(key, line):
    words = line.split()
    for w in words:
        emit(w, 1)  


# input comes from STDIN
import sys

for line in sys.stdin:
  mapper(None, line)
