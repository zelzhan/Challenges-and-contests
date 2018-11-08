'''Given a 32-bit signed integer, reverse digits of an integer.'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        
        1024
        4201
        
        
        """
        negative = False
        if x < 0: 
            x*=-1
            negative = True
        result = 0
        while True:
            result += x%10
            x = x//10
            if x == 0: break
            result *= 10
        if negative: 
            result*=-1
        
        if result < -1 * 2**31 or result > 2**31 - 1: return 0
        return result
            
        
