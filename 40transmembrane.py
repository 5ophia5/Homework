#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix

#KD: the measurement for hydrophobicity
def KD(seq):
	sum = 0
	for aa in seq:
		if aa == 'I': sum += 4.5
		elif aa == 'V': sum += 4.2
		elif aa == 'L': sum += 3.8
		elif aa == 'F': sum += 2.8
		elif aa == 'C': sum += 2.5
		elif aa == 'M': sum += 1.9
		elif aa == 'A': sum += 1.8
		elif aa == 'G': sum += -0.4
		elif aa == 'T': sum += -0.7
		elif aa == 'S': sum += -0.8
		elif aa == 'W': sum += -0.9
		elif aa == 'Y': sum += -1.3
		elif aa == 'P': sum += -1.6
		elif aa == 'H': sum += -3.2
		elif aa == 'E': sum += -3.5
		elif aa == 'Q': sum += -3.5
		elif aa == 'D': sum += -3.5
		elif aa == 'N': sum += -3.5
		elif aa == 'K': sum += -3.9
		elif aa == 'R': sum += -4.5		
	return sum / len(seq)

#hydrophobic region with no prolines
	#hpb = hydrophobic, seq = sequence, w = sequence window size/length, kdt = kd threshold
def hpb(seq, w, kdt):
	for i in range(len(seq) - w):
		win = seq[i : i + w]
		if KD(win) >= kdt and 'P' not in win:
			return True

seq = []
names = []#names of the proteins
proseq = [] #complete protein sequence

signal_win= 8 #length of signal peptide
signal_kdt = 2.5 #KD threshold for signal peptide
hpb_win= 11 #length of hydrophobic region
hpb_kdt = 2.0 #KD threshold for hydrophobic region

with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		if line[0] == '>':
				line = line.rstrip()
				array = line.split()
				names.append(array [0][1:]) #elements of first row; in this case, it is the names
				if len(seq) > 0: proseq.append(' '.join(seq)) #list of complete sequences
				seq = []	
		else:
			seq.append(line) #sequences are added to the seq list, then looped and added to proseq list
	
#print the names of the proteins that meet the conditions		
for name, seq in zip(names, proseq):
	spr = seq[:30] #first 30 aa, spr = signal peptide region
	hpr = seq[30:] #after 30 aa, hpr = hydrophobic region
	if hpb(spr, signal_win, signal_kdt) and hpb(hpr, hpb_win, hpb_kdt):
		print(name)
"""

python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
