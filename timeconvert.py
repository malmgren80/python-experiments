#!/usr/bin/python

import sys

def TimeConvert(num):

	hours = num / 60
	print hours

	minutes = num - (hours * 60)
	print minutes

	output = str(hours) + ':' + str(minutes)
	print output
	return output

TimeConvert(int(sys.argv[1]))