#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    index = 0
    result = 0
    temp = 0
    for c in s:
        if c == 'a':
            temp+=1
    result = (n//len(s)) * temp
    n = n%len(s)
    while index != n:
        if s[index] == 'a':
            result+=1
        index+=1
    return result
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
