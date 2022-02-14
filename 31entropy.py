#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

#empty list
pi = [ ]

#store probabilities into empty list
n = len(sys.argv)
for i in range(1, n):
	pi.append(float(sys.argv[i]))

#doing math to each number on the list
x = [i * math.log2(i) for i in pi]

#taking the negative sum of the outcomes of x
total = 0
for i in x:
	total = total + i
	H = - total
print('%.3f' % (H))

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
