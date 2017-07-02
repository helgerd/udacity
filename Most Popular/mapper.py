#!/home/training/Downloads/Python-2.7.13/python

import sys
import re

p = re.compile(
    '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
    )

for line in sys.stdin:

	m = p.match(line)

	if not m: continue

	host, ignore, user, date, request, status, size = m.groups()
	
	print request.replace('http://www.the-associates.co.uk', '')
