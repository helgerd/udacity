#!/home/training/Downloads/Python-2.7.13/python

import sys

import collections

count = 0

counter = collections.Counter()

for line in sys.stdin:

	data = line.strip().split()
	
	if len(data) != 3: continue


    	counter[data[1]] += 1

print counter.most_common(1)

