#!/bin/python3
import sys

def revisedRussianRoulette(doors):
    min_ = 0
    max_ = 0
    another_doors = []
    another_doors = doors[:]
    for i in range(len(doors)):
        if(i+1 == len(doors)):
            if(doors[i] == 1):
                min_+=1
            break
        if(doors[i] == 1 and doors[i+1] == 1):
            if(doors[i+1] == 1): min_ +=1
            doors[i] = 0
            doors[i+1] = 0
        elif(doors[i] == 1):
            min_+=1
    another_doors = another_doors[::-1]    
    for j in another_doors:
        if(j == 1):
            max_+=1
    list_ = []
    list_.append(min_)
    list_.append(max_)
    return list_


if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)
    print (" ".join(map(str, result)))
