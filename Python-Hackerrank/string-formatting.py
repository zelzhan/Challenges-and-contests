def print_formatted(number):                                        #not the best way to solve this problem
    length = "{:>" + str(len(str(bin(number)))-2) + "}"             #store the string formatting inside the variable length
    for i in range(1, number+1):                                    #ugly code, have no idea how to comment this shit
        print(length.format(i), end = " ")
        print(length.format(str(oct(i))[2:len(str(oct(i)))]), end = " ")
        print(length.format((str(hex(i))[2:len(str(hex(i)))].upper())), end = " ")   
        print(length.format(str(bin(i))[2:len(str(bin(i)))]))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
