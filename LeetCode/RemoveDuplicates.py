class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        vacant, current = 1, 1
        while current < len(nums):
            if nums[current] == nums[current-1]:
                current+=1
                continue
            else:
                nums[vacant] = nums[current]
                vacant+=1
                current+=1
        return vacant
                
            
        
