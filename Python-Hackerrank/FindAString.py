'''In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.''''

def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            counter +=1
            for k in range(len(sub_string)):
                if i+k >= len(string):
                    counter-=1
                    break
                if string[i+k] != sub_string[k]:
                    counter-=1
                    break
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
