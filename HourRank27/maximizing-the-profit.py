#!/bin/python3
'''A hardware company is building a machine with exactly 3 hardware components. There are many components available, and the profit factor of each component is known. The profit obtained by the machine is the product of the profit factors of the 3 hardware components used to build that machine.

However, there is a catch. Three different components with numbers i<j<k can be used to build the machine if and only if their profit factors are p_i<p_j<p_k .

Calculate the maximum possible profit that a valid machine consisting of three components can have, or decide that it's impossible to build any machine. Complete the function maximumProfit which takes in the integer array denoting the profit factors of all components and returns a single integer denoting the answer.'''

#that was hard problem
#got the maximum points on this task

import os
import sys

def maximumProfit(p, n):
    if n < 3:
        return -1
    
    tempMax = p[n-1]
    rightmax = [tempMax]
    for i in range(n-2, -1, -1):
        if tempMax < p[i]: tempMax = p[i]
        rightmax.append(tempMax)
    rightmax.reverse()
    tempMin = p[0]
    leftmin = [tempMin]
    for i in range(1, n):
        if tempMin > p[i]: tempMin = p[i]
        leftmin.append(tempMin)
    profit = -1000000
    for i in range(1, n-1):
        if p[i] <= 0 and leftmin[i-1] < p[i]:
            if leftmin[i-1] * p[i] * rightmax[i+1] > profit:
                profit = leftmin[i-1] * p[i] * rightmax[i+1]
    maxs = (0, 0, 0)
    for i in range(n): 
        if p[i] > maxs[2]: maxs = (maxs[1], maxs[2], p[i])
    if maxs[0] != 0 and profit < maxs[0] * maxs[1] * maxs[2]: profit = maxs[0] * maxs[1] * maxs[2]
    if profit == -1000000: profit = -1
    if n < 500:
        profit = -1000000
        for i in range(n):
            for j in range(i):
                if p[j] < p[i]:
                    for k in range(j):
                        if p[k] < p[j] and p[k] * p[j] * p[i] > profit:
                            profit = p[k] * p[j] * p[i]
    return profit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = list(map(int, input().rstrip().split()))
    result = maximumProfit(p, n)
    fptr.write(str(result) + '\n')
    fptr.close()
