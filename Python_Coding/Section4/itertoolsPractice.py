"""
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

You are given a two lists  A and B. Your task is to compute their cartesian product X.
"""

from itertools import product

a = input()
b = input()

a = list(map(int,a.split()))
b = list(map(int,b.split()))
print(a)
print(b)

result = product(a,b)
print(*result) # use *result to reference result Product list without saving to actual list

