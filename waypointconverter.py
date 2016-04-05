#!/usr/bin/env python

filename = "test.xml"

with open(filename) as fn:
    content = fn.readlines()

print(content)

for count in range(0,len(content)):
    print(count)
