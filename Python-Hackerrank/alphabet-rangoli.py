def print_rangoli(size):
    alph = [chr(ord('a')+i) for i in range(size)]           #alphabetical list comprehensions
    alph.reverse()
    some_list = []
    for i in range(len(alph)):                              #iterate through the length of alphabetical list, append each line to the empty list and print these lines 
        k = 0
        j = i-1
        string1 = ""
        string2 = ""
        while(k != i ):
            string1 += alph[k] + '-'
            string2 += '-' + alph[j]   
            k+=1
            j-=1
        some_list.append((string1 + alph[i] + string2).center(len(alph)*4 - 3, '-'))    #complicated stuff, hard to explain
        print((string1 + alph[i] + string2).center(len(alph)*4 - 3, '-'))
    some_list.reverse()
    for j in some_list[1:]:                                             #list starting with second element
        print(j)      
