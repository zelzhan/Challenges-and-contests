#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
#  [] []     (      )
def isBalanced(s):
    mapping = {'[' : ']', '(' : ')', '{' : '}' }
    stack1 = list(s)
    stack2 = []
    while stack1:
        bracket = stack1.pop()
        if not stack2:
            stack2.append(bracket)
            continue
        
        if bracket in mapping and mapping[bracket] == stack2[-1]:
            stack2.pop()
        else:
            stack2.append(bracket)

    if stack2:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
