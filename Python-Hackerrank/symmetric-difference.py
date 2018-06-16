'''Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.'''
N = input()
set1 = set(map(int, input().split()))
M = input()
set2 = set(map(int, input().split()))
d_set = set()
d_set.update(set1.difference(set2), set2.difference(set1))
print(*sorted(d_set), sep='\n')
