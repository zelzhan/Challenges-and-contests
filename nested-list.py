f __name__ == '__main__':
    some_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        some_list.append([name, score])      #create list
    some_list.sort()                         #sorting the created list called "some_list"
    some_list = dict(some_list)              #transfer "some_list" into the dictionary
    scores = [k for k in some_list.values()] #create another list called "scores" only with values of dictionary "some _list"
    scores = set(scores)                     #transfer "scores" into the set in order to get unique values
    scores = list(scores)                    #transfer to the list
    scores.sort()                            #sort this list
    second_lowest = scores[1]                #finding the second lowest in this list
    
    names = []                               #create another list to store the list of names and sort them in the future
    for j, k in some_list.items():           #iteration through dictionary
        if k == second_lowest:
            names.append(j)
            
    names.sort()                             #sort the list called "names"
    for i in names:
        print(i)
