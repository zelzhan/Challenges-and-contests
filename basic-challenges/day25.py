import math 
input_ = int(input())
list_ = []
for _ in range(input_):
    list_.append(int(input()))

for i in list_:
    if i == 1: 
        print("Not prime")
        continue
    if i < 10:
        for k in range(1, i):
            if i%k == 0 and k != 1: 
                print("Not prime")
                break
            if k == i-1: print("Prime")
    if i < 10: continue
    for j in range(2, int(math.sqrt(i))):
        if i%j == 0 or i%(int(math.sqrt(i)))==0 : 
            print("Not prime")
            break
        if j == int(math.sqrt(i)) - 1: 
            print("Prime")
        
