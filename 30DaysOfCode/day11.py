#!/bin/python3

import sys
import math                                                                                                        #to get - infinity


arr = []
for arr_i in range(6):                                                                                             #input of 2 dimensional array
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]                                              
   arr.append(arr_t)
maxi = -math.inf
temp = maxi

for i in range(4):
    for j in range(4):
        temp = arr[i+1][j+1] + arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] #adding the hourglass
        if(maxi < temp): maxi = temp                                                                               #checking the hourglass with maximum sum
print(maxi)
