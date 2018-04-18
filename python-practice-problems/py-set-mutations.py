'''You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A.'''
_ = input()
s1 = set(input().split())
N = int(input())
for i in range(N):
    plain = input().split()[0]
    if plain == "intersection_update": s1&=set(input().split())
    if plain == "update": s1|=set(input().split())
    if plain == "symmetric_difference_update": s1^=set(input().split())
    if plain == "difference_update": s1-=set(input().split())
print(sum(map(int, s1)))
        
