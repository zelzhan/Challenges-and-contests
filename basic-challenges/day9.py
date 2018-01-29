#!/bin/python3

import sys                                      #fairly easy recursion

def factorial(n):
    if(n == 1):
        return 1
    else:
        return factorial(n-1)*n

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)

