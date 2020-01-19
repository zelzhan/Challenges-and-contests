from collections import defaultdict
class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        hashtable = defaultdict(int)
        for i, string in enumerate(s):
            hashtable[i] = len(string)
            
        
        max_length = max(hashtable.values())
        
        j = 0
        res = []
        
        
        def pop_zeroes(cont):
            i = -1
            while cont[i] == " ":
                cont.pop()
        
        while j != max_length:
            word = []
            for i, string in enumerate(s):
                if hashtable[i] == 0:
                    
                    word.append(" ")
                else:
                    hashtable[i] -=1
                    word.append(string[j])
                
            j+=1
            pop_zeroes(word)
            res.append("".join(word))
            
            
        return res
