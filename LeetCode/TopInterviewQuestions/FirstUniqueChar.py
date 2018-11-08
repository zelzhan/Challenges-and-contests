'''Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.'''

from collections import defaultdict

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        hashtable = defaultdict(int)
        
        for c in s:
            hashtable[c]+=1
            
        for i in range(len(s)):
            if hashtable[s[i]] == 1:
                return i
            
        return -1
        
        
        
