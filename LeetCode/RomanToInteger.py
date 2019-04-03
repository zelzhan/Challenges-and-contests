class Solution:
    def romanToInt(self, s: str) -> int:
        # X I V
        dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = dictionary[s[0]]
        for index in range(1, len(s)):
            prev = dictionary[s[index-1]]
            current = dictionary[s[index]]
            if prev < current:
                res+=current-2*prev
            else:
                res+=current
        return res
                
                
        
