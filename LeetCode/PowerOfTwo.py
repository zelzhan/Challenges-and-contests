'''Given an integer, write a function to determine if it is a power of two.'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        counter=0
        while n:
            if n%2 == 1:
                counter+=1
            if counter == 2:
                return False
            n = n >> 1
        return True
