'''The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.'''
N1 = input()
s1 = set(map(int, input().split()))
N2 = input()
s2 = set(map(int, input().split()))
print(len(s2.union(s1)))


