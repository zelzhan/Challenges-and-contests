class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        counter = 2**k
        
        exists = set()
        
        j = 0
        
        while k <= len(s):
            exists.add(s[j:k])
            k+=1
            j+=1
        
        return len(exists) == counter
        
