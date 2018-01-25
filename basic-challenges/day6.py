 = int(input())
some_list = []                                                      #creation of lists
second_list = []
third_list = []
x = ""                                                              #empty strings
y = ""
for _ in range(a):                                                  #turns user's input into the list 
    some_input = input()
    some_list.append(some_input)
                                                                    
for i in some_list:                                                 #iterates through the provided list and appends the empty strings with even and odd indexes of every iterated strings 
    for j in range(len(i)):
        if(j%2==0):
            x += i[j]
        else:
            y += i[j]
    second_list.append(x)                                           #appends letters with even indexes another list
    third_list.append(y)                                            #appends letters with odd indexes third list
    x = ""
    y = ""
    
for iteration in range(len(some_list)):                             #output
    print(second_list[iteration] + " " + third_list[iteration])

