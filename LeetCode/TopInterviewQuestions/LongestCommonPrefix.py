'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        temp = strs[0]
        for s in strs:
            for i in range(len(s)):
                if i >= len(temp):
                    break
                elif s[i] != temp[i]:
                    temp = temp[:i]
            if len(s) < len(temp):
                temp = s
                    
                    
                    
        return temp
                    
                    
                
        
