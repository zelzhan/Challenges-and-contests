class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                return i
        
        return A[-1]
