class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        counter = 0
        last = 0
        res = ""
        for i, c in enumerate(S):
            if c == "(":
                counter+=1
            else:
                counter-=1
            
            if counter == 0:
                res+= S[last+1:i]
                last = i+1
        
        return res
                
