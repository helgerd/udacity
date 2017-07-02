#!/usr/bin/python

import sys

highestSale = 0.0

oldKey = None

for line in sys.stdin:

	data = line.strip().split("\t")

	if len(data) != 2: continue

	thisKey, thisSale = data

	if oldKey and oldKey != thisKey:
		print oldKey, "\t", highestSale
		highestSale = 0.0

	oldKey = thisKey
	if float(thisSale) >= highestSale:
		highestSale = float(thisSale)

if oldKey != None:
	print oldKey, "\t", highestSale
