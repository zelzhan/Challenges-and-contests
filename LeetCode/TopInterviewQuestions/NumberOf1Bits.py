'''Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        counter = 1
        while n//2 != 0:
            counter += n%2
            n = n//2
            
        return counter
        
