'''Reverse a string'''

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        '''solution 1: Beats 1.67% Python solutions'''
        # res = ""
        # for i in s:
        #     res = i + res
        # return res
    
    
        '''solution 2: Beats 31.42% Python solutions'''
        # return s[::-1]
    
    
        '''solution 3: two pointers technique. Beats 40.43% of Python solutions'''
        first = 0
        second = len(s) - 1
        s1 = list(s)        
        while second - first >=1:
            temp = s1[first]
            s1[first] = s1[second]
            s1[second] = temp
            first +=1
            second-=1
        return "".join(s1)
            
    
    
