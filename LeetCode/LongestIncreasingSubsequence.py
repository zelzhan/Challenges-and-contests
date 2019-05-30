class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # step 1: identify changing vairables
        
        # [ 10, 19, 2, 5, 3, 7, 101, 18]
        #    1   2  1  2  2  3    4  4 
        
        # 1) array position
            
        # step 2: clearly state recurrence relation
            
        # f(i) = max(from f(0) to f(i-1) + 1) 
            
        # step 3: base case
        
        # f(0) = 1
        
        # step 4: implement
        
        if not nums:
            return 0
        
        memo = [1] * len(nums)
        res = 1
        
        
        for current in range(len(nums)):
            for i in range(current):
                
                if nums[i] < nums[current] and memo[i]+1 > memo[current]:
                    
                    memo[current] = memo[i]+1
                            
                    # save the result
                    if memo[i]+1 > res:
                        res = memo[i]+1
                
        return res
        # step 5: time complexity
    
        # time O(N^2)
        # space O(N)
