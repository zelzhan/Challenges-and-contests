class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        memo = {}
        
        def traverse(i, cur, target):
            
            if (i, cur) in memo:
                return memo[(i, cur)]
            
            if i == len(nums) and cur == target:
                return 1
            elif i == len(nums):
                return 0
            
            memo[(i+1, cur+nums[i])] = traverse(i+1, cur+nums[i], target) 
            memo[(i+1, cur-nums[i])] = traverse(i+1, cur-nums[i], target)
            return memo[(i+1, cur+nums[i])] + memo[(i+1, cur-nums[i])] 
            
        return traverse(0, 0, S)
