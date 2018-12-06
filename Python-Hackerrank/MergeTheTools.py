'''https://www.hackerrank.com/challenges/merge-the-tools/problem'''
def merge_the_tools(string, k):
    sublists = [string[i:i+k] for i in range(0, len(string), k)]
    res = []
    for list in sublists:
        hashtable = {}
        for l in list:
            if l not in hashtable:
                hashtable[l] = 0
            hashtable[l]+=1
        temp = ""
        for l in list:
            if hashtable[l] == -1:
                continue
            temp += l
            hashtable[l] = -1
        res.append(temp)
    for r in res:
        print(r)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
