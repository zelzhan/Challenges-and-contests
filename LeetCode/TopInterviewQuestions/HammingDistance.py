'''The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        minim, maxim = (x, y) if x < y else (y, x)
        while minim != 0:
            if minim%2 != maxim%2:
                res += 1
            minim = minim // 2
            maxim = maxim // 2
            
        while maxim != 0:
            if maxim%2 == 1:
                res+=1
            maxim = maxim // 2
            
        return res
        
        
