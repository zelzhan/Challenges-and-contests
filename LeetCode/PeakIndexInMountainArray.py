'''Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].'''

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # naive solution
        for i in range(len(A)-1):
            print(A[i], A[i+1])
            if A[i+1] < A[i]:
                return i
        return A[-1]
        
        lo , hi = 0, len(A) - 1
        
        while hi > lo:
            mid = int(lo + (hi - lo)/2)
            if A[mid+1] > A[mid]:
                lo = mid+1
            else:
                hi = mid
        return hi
