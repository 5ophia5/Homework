#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

size = int(sys.argv[1])
num = int(sys.argv[2])
length = int(sys.argv[3])

coverage = []
for i in range(size): coverage.append(0)
for i in range(num): #for each read number
	p = random.randint(1, size) #randomize starting position
	if p < (size - length): #cannot sample the ends bc read length would be longer than genome size
		for j in range(p, p + length):
			coverage[j] += 1 #add 1 everytime the same nt is read again

coverage.sort()

#average coverage
total = 0
for k in coverage:
	total = total + k
avg = total / size

#min, max, and avg coverage
print(coverage[0], coverage[-1], avg)





"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
