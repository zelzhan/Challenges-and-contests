tring(string, position, character): #another easy problem
    string = list(string)
    string[position] = character
    string = ''.join(string)
    return string
