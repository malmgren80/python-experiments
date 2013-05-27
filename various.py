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


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'

def add(a,b):
	result = a+b
	print result
	list = [result]
	def sub():
		c = a - b 
		print c
		list.append(c) # not possible to modify result here, but possible to modify mutable list
	sub()
	
	print list

add(10, 20)