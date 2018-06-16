N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):                  #knowledge is power!
    print((".|."*i).center(M, '-'))     #the solution of this challenge based on knowledge of method "Center with attributes 'size' and 'filter'"
print("WELCOME".center(M, '-'))
for i in range(N-2,-1,-2): 
    print((".|."*i).center(M, '-'))
