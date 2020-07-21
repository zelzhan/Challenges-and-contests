class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = [0]
                
        def expand(word, left, right):

            if left < 0 or right == len(s) or s[right] != s[left]:
                return
            
            counter[0]+=1
            expand(s[left] + word + s[right], left-1, right+1)
            
        
        for i in range(2*len(s)):
            if i%2 == 0:
                i//=2
                expand(s[i], i-1, i+1)
            else:
                i//=2
                expand("", i, i+1)
            
        return counter[0] + len(s)
