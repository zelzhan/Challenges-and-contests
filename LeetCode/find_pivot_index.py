class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #   _
        # 1 7 3 6 5 6
        # 0 | 1 | 27
        # 1 | 7 | 20
        # 8 | 3 | 17
        # 11| 6 | 11
        # 17| 5 | 6
        # 23| 6 | 0
        
        left = 0 
        right = sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            
            if left == right:
                return i
            
            left += nums[i]
            
        return -1
