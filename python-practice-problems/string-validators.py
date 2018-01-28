if __name__ == '__main__':
    s = input()
        
    for alphanum in range(len(s)):
        if(s[alphanum].isalnum()):                #is string contains any aphanumeric characters
            print("True")
            break
        elif(alphanum == len(s)-1):
            print("False")
            break
        
        
    for i in range(len(s)):                       #is string contains any alphabetic characters
        if(s[i].isalpha()):
            print("True")
            break
        elif(i == len(s) - 1):
            print("False")
            break

    for j in range(len(s)):
        if(s[j].isdigit()):                        #is string contains any digits
            print("True")
            break
        elif(j == len(s) - 1):
            print("False")
            break
        
    
    for lower in range(len(s)):
        if(s[lower].islower()):                     #is string contains any lowercase characters           
            print("True")
            break
        elif(lower == len(s) - 1):
            print("False")
            break
        
    
    for upper in range(len(s)):
        if(s[upper].isupper()):                     #is string contains any uppercase characters
            print("True")
            break
        elif(upper == len(s)-1):
            print("False")
            break
        
    
    

