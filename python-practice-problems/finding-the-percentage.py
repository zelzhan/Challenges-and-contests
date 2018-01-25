f __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()     #turns first input into the key and other inputs as listed values for this key
        scores = list(map(float, line))   #turns the list of values into the float 
        student_marks[name] = scores      #definition of dictionary 
    query_name = input()                  #input of testing key
    for i, j in student_marks.items():    #iteration through the keys and values simultaniously 
        if(query_name == i):
            a = (j[0]+j[1]+j[2])/3        #some mathematical stuff
    print("{:0.2f}".format(a))            #string formating with 2 decimal places


