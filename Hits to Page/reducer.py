#!/usr/bin/python

import sys

count = 0

for line in sys.stdin:

	data = line.strip().split()
	
	if len(data) != 3: continue

	if data[1] == "/assets/js/the-associates.js":

		count += 1

print count
