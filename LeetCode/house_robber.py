class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 2   7   9   -3    -1     5   2 
        # 2   7   11   11    11   16   16  
       
    
        if not nums:
            return 0
        
        memo = [0] * len(nums)
        for i in range(len(nums)):
            if i > 1:
                memo[i] = max(memo[i-2]+nums[i], memo[i-1])
            else:
                memo[i] = max(nums[i], memo[i-1])     
        
        return memo[-1]
                
                
            
