#!/usr/bin/python

import sys

count = 0

for line in sys.stdin:

	data = line.strip().split()
	
	if len(data) != 4: continue

	if line.strip() == "10.99.99.186":

		count += 1

print count
