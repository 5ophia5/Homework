# mcb185.py

import sys
import gzip
import math

#read fasta file
def read_fasta(filename):
	name = None
	seqs = []

	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

# def other functions...

#try seq = 'ACGTACGTGGGGTTTTTACGTAGGGACCCATTATAAAACGTGCATGATGTGTGACAC'

#Shannon entropy
def shannon_entropy (seq):
	n = len(seq)
	#the counts of each nucleotide in the sequence
	count_a = 0
	count_c = 0
	count_g = 0
	count_t = 0
	
	for nt in seq:
		if nt == 'A': count_a += 1
		if nt == 'C': count_c += 1
		if nt == 'G': count_g += 1
		elif nt == 'T': count_t += 1
		
	#frequency of each nucleotide in the sequence
	pi = []

	pi_a = count_a / n
	pi_c = count_c / n
	pi_g = count_g / n
	pi_t = count_t / n
	
	#put all frequencies in a list
	pi.append(pi_a)
	pi.append(pi_c)
	pi.append(pi_g)
	pi.append(pi_t)
	
	#shannon entropy calculation
	entropy = 0
	for i in pi:
		if i > 0: entropy += (-(i * math.log2(i)))
	return entropy

#N-based masking
def N_mask (seq, w, threshold):
	newseq = list(seq) #put sequence in a list
	masked = ''
	for i in range (len(seq) - w + 1): #look at sequence in fragments with window size w
		window = list(seq[i: i + w])
		if shannon_entropy (window) < threshold: #change nucleotides into N if the entropy of the fragment is lower than the threshold
			for nt in range(len(window)):
				newseq[i + nt] = 'N'
				masked = "".join(newseq) #change the sequence list into a string
	return masked
	
#Lowercase masking 
def low_mask (seq, w, threshold):
	newseq = list(seq) #pu sequence in a list
	masked = ''
	for i in range(len(seq) - w + 1): #look at sequence in fragments with window size w
		window = seq[i: i + w]
		if shannon_entropy (window) < threshold: #change nucleotides into lowercases if the entropy of the fragment is lower than the threshold
			for nt in range(len(window)):
				if window[nt] == 'A': newseq[i + nt] = 'a'
				elif window[nt] == 'C': newseq[i + nt] = 'c'
				elif window[nt] == 'G': newseq[i + nt] = 'g'
				elif window[nt] == 'T': newseq[i + nt] = 't'
				masked = "".join(newseq) #change the sequence list into a string
	return masked

#try print(N_mask(seq, 3, 1))
#try print(low_mask(seq, 3, 1))

