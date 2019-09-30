#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the maximumToys function below.
def maximumToys(prices, k):
    heapq.heapify(prices)
    res = 0
    while True:
        k -= heapq.heappop(prices)
        if k < 0:
            break
        res+=1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
