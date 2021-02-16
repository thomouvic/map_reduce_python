#!/usr/bin/env python
"""reducer.py"""

def emit(key, value):
  print('%s\t%s' % (key, value))

def reducer(w,li):
  emit(w, sum([int(i) for i in li]))



# input comes from STDIN
# process input into lists for each key
import sys

current_key = None
current_list = []

for line in sys.stdin:
    key, value = line.split('\t', 1)
    value = value.strip()

    if current_key == key:
        current_list += value
    else:
        if current_key:
          reducer(current_key,current_list)
        current_key = key
        current_list = [value]

# don't forget the last key!
if current_key == key:
    reducer(current_key,current_list)
