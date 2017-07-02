#!/usr/bin/python

import sys

totalSale = 0.0

numSale = 0

for line in sys.stdin:

	totalSale += float(line)

	numSale += 1

print "{0}\t{1}".format(totalSale, numSale)
