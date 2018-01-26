wap_case(s):
    string = ""                 #empty string
    for i in s:                 #iterate each character in string
        if(i == i.lower()):     #checking whether the character is equal to the lowercase of this character
            i = i.upper()
        elif(i == i.upper()):   #same check but with uppercase
            i = i.lower()
        string += i             #string concatenation with iterated character
    return string               

