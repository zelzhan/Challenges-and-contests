class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        res =  0
        counter = 0
        for c in s:
            if c == 'L':
                counter-=1
            else:
                counter+=1
            
            if counter == 0:
                res+=1
                
        return res
