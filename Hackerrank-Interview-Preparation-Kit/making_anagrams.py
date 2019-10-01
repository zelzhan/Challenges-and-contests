#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the makeAnagram function below.
# a b c d
# b c f k
# 8 - 2 = 6
# diff 2
# 
# o w m a n e 

def makeAnagram(a, b):
    hashtable1 = defaultdict(int)
    hashtable2 = defaultdict(int)

    for el in a:
        hashtable1[el] += 1

    for el in b:
        hashtable2[el] += 1

    res = 0
    for key, _ in hashtable1.items():
        while hashtable1[key] != 0:
            if hashtable2[key]:
                hashtable2[key]-=1
            else:
                res+=1
            hashtable1[key] -= 1

    return res + sum(hashtable2.values())

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
