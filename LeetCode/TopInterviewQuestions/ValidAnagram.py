'''Given two strings s and t , write a function to determine if t is an anagram of s.'''

from collections import defaultdict

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashtable = defaultdict(int)
        hashtable2 = defaultdict(int)
        
        if len(t) != len(s): return False
        
        for c in s:
            hashtable[c]+=1
            
        for k in t:
            hashtable2[k] +=1
            
        for key, value in hashtable2.items():
            if hashtable[key] != value:
                return False
        return True
