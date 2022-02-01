#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

r = dna[::-1] 
for i in range(len(r)):
	a = r[i]
	if a == 'A': print('T', end='')
	elif a == 'C': print('G', end='')
	elif a == 'T': print('A', end='')
	elif a == 'G': print('C', end='')
"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
