#!/bin/python3
import sys
S = input().strip()         #input
try:            
    int(S)                  #trying to convert string into integer
    print(S)
except ValueError:          #In case of ValueError(String-to-integer error is ValueError) prints "Bad String"
    print("Bad String")


