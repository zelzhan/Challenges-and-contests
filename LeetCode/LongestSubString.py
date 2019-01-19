'''https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_counters = []
        length = 0
        s = s + "k"
        for c in s:
            i = 0
            for counter in list_counters:
                if len(counter) > length:
                    length = len(counter)
            while i < len(list_counters):
                list_counters[i].append(c)
                if c in list_counters[i][:-1]:
                    list_counters.remove(list_counters[i])
                    i-=1
                i+=1
            list_counters.append([c])
        return length
            
        
        
        
        
        
