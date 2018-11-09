'''Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.'''

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "": return 0
        satisfied = False
        
        for i in range(len(haystack)):
            start = 0
            if i + len(needle) > len(haystack):
                return -1
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if haystack[i+j] != needle[j]:
                        break
                    if j == len(needle) -1: satisfied = True
                    
                if satisfied:
                    return i
                
        return -1
