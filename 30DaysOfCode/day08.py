def dictionary():                                       #Warning, partial solution
    numberOfEntries = int(input())                      #number of entries - N
    someList = []                                       #creation of empty list
    for _ in range(numberOfEntries):                    #append "someList" with input and creation of nested list
        anotherList = input().split()
        someList.append(anotherList)
    dic = dict(someList)                                #turning the nested list into the dictionary
    while(True):                                        #infinite loop, breaks if input is empty
        try:                
            someInput = input()                         
        except EOFError:
            break
        if(someInput not in dic.keys()):                #if input not in the dictionary, prints "Not found"
            print("Not found")
        for key in dic:                                 #iteration through the keys of dictionary
            if(key == someInput):
                print(someInput + "=" + dic[key])
                break
                
if __name__ == '__main__':
    dictionary()
