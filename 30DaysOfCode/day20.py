#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numSwaps = 0
for i in range(n):                                          #bubble sort implementaton (nested loop)
    for j in range(n):
        if(j+1 == n): break
        if(a[j] > a[j+1]):
            numSwaps+=1
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            
print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n-1]))

