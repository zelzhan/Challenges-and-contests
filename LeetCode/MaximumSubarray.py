import sys
class Solution:
    # -2  1 -3  4 -1 -1  2  1 -5  4
    def maxSubArray(self, nums: List[int]) -> int:
        res = -(sys.maxsize+1)
        maxneg = -(sys.maxsize+1)
        cur = 0
        for num in nums:
            if num > maxneg:
                maxneg = num
            cur += num
            if cur < 0:
                cur = 0
            elif cur > res:
                res = cur
        if maxneg>res:
            return maxneg
        return res
            
        
