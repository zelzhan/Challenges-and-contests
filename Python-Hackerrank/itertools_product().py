'''You are given a two lists A and B. Your task is to compute their cartesian product AxB.'''
from itertools import product

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
lst = " ".join(map(str, product(list1, list2)))
print(lst)
