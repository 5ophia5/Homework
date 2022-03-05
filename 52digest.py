#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments

#reads file function
def readgen(filename):
	found_origin = False
	with open (filename) as fp:
		seq = ''
		for line in fp.readlines():
			if 'ORIGIN' in line:
				found_origin = True
			if found_origin == True:
				words = line.split()
				for word in words[1:]:
					seq += word
	return seq

#digest function that outputs the sizes of the restriction fragments
def digest(filename, pattern):

	#read file
	seq = readgen(filename)

	#find the pattern in the sequence
	start = [ ]
	for match in re.finditer(pattern, seq):
				#print(match.group(), match.start(), match.end())
		a = match.start() #starting positions
		start.append(a) #add all starting positions into a list

	#first fragment
	print(start[0])
	#print(start[0] + 1)

	#list of sizes of fragments in the middle
	diff_start = []
	i = 0
	for i in range(1, len(start)):
		x = start[i] - start[i-1]
		diff_start.append(x)
	for midseg in diff_start:
		print(midseg)

	#last fragment
	#print(len(seq) - start[-1] - 1)

digest(sys.argv[1], sys.argv[2])

"""
#Notes:
#seq = readgen(filename)	

#def test(filename, pattern):
	#readgen(filename)
	
#test(sys.argv[1], "gaattc")
"""

"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
