#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

stats = [ ]

x = len(sys.argv)
for i in range(1, x):
	stats.append(float(sys.argv[i]))

#Count
n = len(stats)
print('Count:', n)

#Minimum
stats.sort()
print('Minimum:', '%.1f' % (stats[0]))

#Maximum
print('Maximum:', '%.1f' % (stats[-1]))

#Mean
total = 0
for i in stats:
	total = total + i
avg = total / n
print('Mean:', '%.3f' % (avg))

#Standard deviation
dev = [(x - avg) ** 2 for x in stats]
sumdev = 0
for i in dev:
	sumdev = sumdev + i
var = sumdev / n
std = math.sqrt(var)
print('Std.dev:', '%.3f' % (std))

#Median
if n % 2 == 0: #for even-numbered lists
	m1 = int((n / 2)  - 1)
	m2 = int((n /2) + 1)
	print('Median:', stats[m1])
else: #for odd-numbered lists
	m = int(n / 2)
	print('Median:', '%.3f' % stats[m])

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
