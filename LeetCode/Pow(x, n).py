'''Implement pow(x, n), which calculates x raised to the power n (xn).'''

class Solution(object):
    
    def helper(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        temp = self.helper(x, n/2)
        if n%2 == 0:
            return temp*temp
        else:
            return x*temp*temp
        
        
    def myPow(self, x, n):
        negative = True if n < 0 else False
        if negative:
            n = -n
        temp = self.helper(x, n)
        if negative:
            return 1/temp
        else:
            return temp
            
