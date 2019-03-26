#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    result = 0
    hashtable = defaultdict(int)
    for element in ar:
        if (hashtable[element] + 1)%2 == 0:
            result+=1
        hashtable[element] = (hashtable[element] + 1)%2
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
