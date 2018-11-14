'''Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0: x = -x
        hi, lo = 2**31 -1, 0
        while hi > lo:
            mid = int(lo + (hi - lo)/2)
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                hi = mid
            else:
                lo = mid + 1
        return hi - 1
