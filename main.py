#!/usr/bin/python

import sys
import functools

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if len(sys.argv) < 4 or len(sys.argv) > 4:
    print("Exactly 3 numbers are required")
    exit()

a, b, c, *extra = sys.argv[1:]

lis = [int(n) for n  in [a, b, c]]

lis2 = [0 if 13 <= x <= 19 and x not in [15, 16] else x for x in lis]

s = functools.reduce(lambda x, y: x + y, lis2)

print("s", s)

