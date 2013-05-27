#!/usr/bin/python

import sys

a = ['spam', 'eggs', 100, 1234]
print a

# Replace some items:
a[0:2] = [1, 12]
print a

# Remove some:
a[0:2] = []
print a

# Insert some:
a[1:1] = ['bletch', 'xyzzy']
print a

for x in range(5):

	print x

	if x == 0:
		print 'Zero'
	elif x % 2 != 0:
		print 'Uneven'
	else:
		print 'Even'