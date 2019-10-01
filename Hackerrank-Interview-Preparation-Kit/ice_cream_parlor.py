#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
# Complete the whatFlavors function below.
# 1 2 3 4 5
def whatFlavors(cost, money):
    hashtable = defaultdict(int)
    for index, price in enumerate(cost):
        hashtable[price] = index

    
    for i, price in enumerate(cost):
        diff = money - price
        if diff in hashtable and hashtable[diff] != i:
            print(i+1, hashtable[money-price]+1)
            return
    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
