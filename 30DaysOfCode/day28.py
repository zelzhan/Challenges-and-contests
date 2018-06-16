#!/bin/python3
'''Consider a database table, Emails, which has the attributes First Name and Email ID. 
Given N rows of data simulating the Emails table, print an alphabetically-ordered list
of people whose email address ends in @gmail.com.'''
import re
import sys

list_ =[]
N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.search('@gmail\.com$',emailID): list_.append(firstName)
print(*sorted(list_), sep='\n')

