#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 5
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
