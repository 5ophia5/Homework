#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

gc = 0
for nt in dna:
	if nt == 'G' or nt == 'C': gc +=1 #cleanest and most simplest way
print('%.2f' % (gc/len(dna)))
print('{:.2f}'. format(gc/len(dna)))
print(f'{((gc/len(dna))):.2f}')

"""
#alternatively:
gc = 0
for nt in dna:
	if nt == 'G': gc += 1
	elif nt == 'C': gc += 1
print('%.2f' % (gc/len(dna)))
print('{:.2f}'. format(gc/len(dna)))
print(f'{((gc/len(dna))):.2f}')
"""

"""
python3 21gc.py
0.42
0.42
0.42
"""
