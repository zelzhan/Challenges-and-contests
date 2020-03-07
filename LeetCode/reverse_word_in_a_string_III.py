class Solution:
    def reverseWords(self, s: str) -> str:
        
        def reverse_word(string):
            i, j = 0, len(string) - 1 
            string = list(string)
            while i < j:
                string[i], string[j] = string[j], string[i]
                i+=1
                j-=1
            
            return "".join(string)
        
        res = []
        for word in s.split():
            res.append(reverse_word(word))
            
        return res
