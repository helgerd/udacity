#!/usr/bin/python

import sys

for line in sys.stdin:

    data = line.strip().split("\t")

    if len(data) != 6: continue

    date, time, store, product, cost, payment = data

    print "{0}\t{1}".format(product, cost)
