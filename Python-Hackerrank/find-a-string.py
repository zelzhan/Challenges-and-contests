def count_substring(string, sub_string):                            #WARNING! this is only partial solution
    counter = 0                                                     #I'll comment this code after completion of the task
    second_counter = 0
    restrictor = 0
    
    for i in range(len(string)):
        restrictor += 1
        if(string[i] == sub_string[0]):
            for j in range(len(sub_string)):
                if(len(sub_string) > len(string) - restrictor):
                    break
                if(sub_string[j] == string[i+counter]):
                    counter += 1
                if(counter == len(sub_string)):
                    second_counter += 1
                    counter = 0
                    break
    return second_counter + 1
