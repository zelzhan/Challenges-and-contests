#!/bin/python3

import sys


n = int(input().strip())

string = ""                                                     #creating empty string

while(n > 0):                                                   #implementation of loop, which will convert decimal to binary (in reverse order)
    remainder = n%2 
    string += str(remainder)
    n = int(n/2)
    
reverse = string[::-1]                                          #reverse the string in order to obtain real binary representation 
counter = 1
maximum = 1
for i in range(len(reverse)):
    if(i+1 == len(reverse)):                                    #if the next element of loop will be greater than length of the string, break the loop. Otherwise it will cause index out of range error
        break
    if((reverse[i] == reverse[i+1]) and (reverse[i] == '1')):   #checking whether the string is equal to "1" and the next element is equal to the previous 
        counter+=1
        if(counter > maximum):
            maximum = counter
    else:
        counter = 1                                             #set counter to one
        
print(maximum)
        
        
        
    

    
