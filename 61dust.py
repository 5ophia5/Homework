#!/usr/bin/env python3
# 61dust.py

import mcb185
import argparse

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(description='Reads FASTA file and outputs sequences with lowercases or N-bases.')

parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='requires sequence (fasta) file')
parser.add_argument('--winsz', required=True, type=int,
	metavar='<int>', help='requires window size')
parser.add_argument('--hthresh', required=True, type=float,
	metavar='<float>', help='requires shannon entropy (H) threshold')

# switches
parser.add_argument('--lowercase', action='store_true',
	help='default is N-based masking, then converts sequences to lowercases')

# finalization
arg = parser.parse_args()

#default output is N-based masking, --lowercase for lowercase masking
masked = ''
for name, seq in mcb185.read_fasta(arg.fasta):
	if arg.lowercase: masked = mcb185.low_mask(seq, arg.winsz, arg.hthresh)
	else: masked = mcb185.N_mask(seq, arg.winsz, arg.hthresh)
	print(masked)
	
#command line: python3 61dust.py --fasta ../MCB185-2022/Data/chr1.fa --winsz 30 --hthresh 1.3 
# or: python3 61dust.py --fasta ../MCB185-2022/Data/chr1.fa --winsz 30 --hthresh 1.3 --lowercase


