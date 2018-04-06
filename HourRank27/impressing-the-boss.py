#!/bin/python3
'''Given the consecutive years' sales data of a company as an array of integers: a = [a0, a1, ... a(n-1)] , with a_i  denoting the total sales during the "i"th year, your current task is to present the annual sales graph.

Your boss would be most impressed if the sales graph showed that the total sales never decreased for every pair of consecutive years. For this, you are allowed to modify at most one element of the data array for the property to be true. (Any more and the change will be too obvious.)

Given a, determine if it is possible to do this task.

Complete the function canModify which takes in the integer array a and returns the string YES or NO denoting whether it is possible to do the task.'''

#This competetition is not counted due to the wrong construction of tests, it was not counted for contest
#not working solution

import os
import sys
def canModify(a):
    for i in range(len(a)):
        if i+1 == len(a): break
        if a[i+1] < a[i]:
            if i+2 == len(a):
                a[i+1] = a[i+2] + 1 
                break
            print(i)
            a[i+1] = a[i+2] - 1
    if a == a.sort():
        return "Yes"
    return "No"
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    for i in range(n*2):
        a = list(map(int, input().rstrip().split()))
        print(a)
        result = canModify(a)
        fptr.write(result + '\n')
    fptr.close()

