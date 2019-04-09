class Solution:
    # 1
    # 11
    # 21
    # 1211
    # 111221
    # 312211
    # 13112221
    def countAndSay(self, n: int) -> str:
        state = ['1']
        n-=1
        while n:
            counter = 1
            index = 1
            res = []
            while index < len(state):
                if state[index] == state[index-1]:
                    counter+=1
                elif counter == 1:
                    res.append('1')
                    res.append(state[index-1])
                else:
                    res.append("{}".format(counter))
                    res.append(state[index-1])
                    counter=1
                index+=1
            res.append("{}".format(counter))
            res.append(state[-1])
            state = res
            n-=1
        return "".join(state)
                
        
