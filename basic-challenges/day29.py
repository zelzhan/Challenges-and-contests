#!/bin/python3
'''Given set S = {1, 2, 3 ..., N}. Find two integers, A and B (where A<B), from set S such that the value of A&B is the maximum possible and also less than a given integer, K. In this case, & represents the bitwise AND operator.'''

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = map(int, input().split())
    print(k-1) if (k-1|k) <= n else print(k-2)

