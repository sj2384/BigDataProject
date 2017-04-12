#!/usr/bin/python
import sys
import csv 

for item in csv.reader(sys.stdin):
	print '%s\t%d' % (item[9],1)
