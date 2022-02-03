#!/usr/bin/env python3

import random
# comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

dna = ' '
length = 30
fraction = 0.6
random.seed() 
for i in range (length):
	if random.random() < fraction:
		if random.random() < 0.5: dna += 'A'
		else: 				      dna += 'T' 
	else: 
		if random.random() < 0.5: dna += 'G'
		else: 				      dna += 'C'

at = 0
for i in range(len(dna)):
	if dna[i] == 'A': at += 1
	elif dna[i] == 'T': at += 1

print(length, at/len(dna), dna)


"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
