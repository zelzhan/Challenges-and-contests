from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        table1 = defaultdict(list)
        table2 = defaultdict(list)
        
        i = 0
        for c1, c2 in zip(s, t):
            table1[c1].append(i)
            table2[c2].append(i)
            i+=1
            
        
        for i in range(len(s)):
            if table1[s[i]] != table2[t[i]]:
                return False
            
        
        return True
