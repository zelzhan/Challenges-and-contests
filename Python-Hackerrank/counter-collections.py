'''Raghu is a shoe shop owner. His shop has X number of shoes. 
He has a list containing the size of each shoe he has in his shop. 
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.'''

from collections import Counter

num_shoes = int(input())
sizes = input().split()
num_cust = int(input())
purch_list = [input().split() for i in range(num_cust)]
purch = [purch_list[i][0] for i in range(num_cust)]
counter = dict(Counter(sizes))
res = 0

for j in range(num_cust):
    if purch[j] in sizes and purch[j] in counter:
        for k in purch_list:
            if k[0] == purch[j]: 
                res+=int(k[1])
                purch_list.remove(k)
                break
        counter[purch[j]]-=1
        if counter[purch[j]] == 0:
            del counter[purch[j]]
print(res)
