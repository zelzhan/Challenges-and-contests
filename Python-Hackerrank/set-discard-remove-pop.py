'''You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.
'''

n = int(input())
s = set(map(int, input().split())) 
N = int(input())
for i in range(N):
    input_ = input()
    if input_ == "pop":
        s.pop()
    elif input_[:6] == "remove":
        s.remove(int(input_.split()[1]))
    else:
        s.discard(int(input_.split()[1]))
print(sum(s))
