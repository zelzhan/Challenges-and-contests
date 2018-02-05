#!/bin/python3

import sys

def acidNaming(acid_name):
    if(acid_name[:5] == "hydro" and acid_name[:-3:-1] == 'ci'):
        return "non-metal acid"
    elif(acid_name[:-3:-1] == 'ci'):
        return "polyatomic acid"
    else:
        return "not an acid"

if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        acid_name = input().strip()
        result = acidNaming(acid_name)
        print(result)

