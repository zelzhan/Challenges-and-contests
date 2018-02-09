list_ = [list(i) for i in string.split()]  
    for letter in list_:
        letter[0] = letter[0].upper()
    list_ = [''.join(j) for j in list_]
    list_ = ' '.join(list_)
    return list_

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)

