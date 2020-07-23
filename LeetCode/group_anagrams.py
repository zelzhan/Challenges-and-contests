from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        counters = []
        
        for string in strs:
            counter = Counter(string)
            found = False
            for i, c in enumerate(counters):
                if c == counter:
                    res[i].append(string)
                    found = True
                    break
                    
            if not found:
                counters.append(counter)
                res.append([string])
                
        return res
