from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        c1 = Counter(p)
        c2 = Counter(s[:len(p)])
        
        i, j = 0, len(p)
        
        def compare(c1, c2):
            for key, value in c1.items():

                if c2[key] != value:
                    return False
            return True
        
        
        res = []
        if compare(c1, c2):
            res.append(0)
        
        while j < len(s):
            c2[s[i]]-=1
            c2[s[j]]+=1
            
            if compare(c1, c2):
                res.append(i+1)
            
            i+=1
            j+=1
        
        return res
