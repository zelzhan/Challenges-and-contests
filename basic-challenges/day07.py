#!/bin/python3
import sys

n = int(input().strip())                                            #some input stuff
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
counter = len(arr) - 1                                              #setting the counter
for _ in range(len(arr)):                                           #loop iteratingo through lenght of array
    print(str(arr[counter]) + " ", end = '')                        #do not print the number on next line
    counter -= 1                                                    

