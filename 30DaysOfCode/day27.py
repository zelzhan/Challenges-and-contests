def printf(n, k, a):                            #dumbest problem
    print(str(n) + " " + str(k))
    print(" ".join(map(str, a)))

print(5)
printf(4, 3, [-1, 0, 4, 2])
printf(5, 2, [0, -1, 2, 1, 4])
printf(7, 6, [2, 0, -1, 1, 1, 1, 1])
printf(3, 1, [-1, 0, 4])
printf(6, 4, [0, -1, 1, 4, 5, 6])


