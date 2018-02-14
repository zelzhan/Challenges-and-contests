def minion_game(string):
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in "AEIOU":    kevin += (len(string)-i)
        else:   stuart += (len(string)-i)
    if kevin > stuart:  print("Kevin "+str(kevin))
    elif kevin < stuart:    print("Stuart " + str(stuart))
    else:   print("Draw")            
