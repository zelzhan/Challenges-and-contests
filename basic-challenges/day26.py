str1 = input().split()
str2 = input().split()

if str1[1] == str2[1] and str1[2] == str2[2] and int(str1[0])>int(str2[0]):
    fine = int(str1[0]) - int(str2[0])
    print(15*fine)
elif str1[2] == str2[2] and int(str1[1]) > int(str2[1]):
    fine = int(str1[1]) - int(str2[1])
    print(500*fine)
elif str1[2] > str2[2]: print(10000)
else: print(0)


