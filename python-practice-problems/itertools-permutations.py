'''You are given a string S. 
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.'''

from itertools import permutations

string = input().split()
perm_list = list(map(list, permutations(string[0], int(string[1]))))
for i in range(len(perm_list)):
    perm_list[i] = "".join(perm_list[i])
print("\n".join(sorted(perm_list)))
    

