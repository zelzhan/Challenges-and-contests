class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # 1 3 4 2 2
        # first = 2
        # second = 2
        
        first = nums[0] 
        second = nums[nums[0]]
        
        while first != second:
            first = nums[first] 
            second = nums[nums[second]]
        
        second = 0
        
        while first != second:
            first = nums[first] 
            second = nums[second]
            
        return first
        
