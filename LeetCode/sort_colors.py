class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        # 1 0 0 1 1 0
        # l r  
        # 0 0 0 1 1 1
        #           r
        #     l
        
        # 0 1 2 1
        #   r    
        # l          
        #     m
        
        # swap zero if 1 or 2 are smaller
        # swap one if 2 is smaller
        
        
        zero, one, two = 0, 0, 0
        
        while zero < len(nums) and nums[zero] != 0:
            zero+=1
        
        while one < len(nums) and nums[one] != 1:
            one+=1
            
        while two < len(nums) and nums[two] != 2:
            two+=1
        
        while zero < len(nums):
            if one < two < zero or one < zero < two:
                nums[one], nums[zero] = nums[zero], nums[one]
                while one < len(nums) and nums[one] != 1:
                    one+=1
            elif two < one < zero or two < zero < one:
                nums[zero], nums[two] = nums[two], nums[zero]
                while two < len(nums) and nums[two] != 2:
                    two+=1
            else:
                zero+=1
            while zero < len(nums) and nums[zero] != 0:
                zero+=1
        
        
        
        while one < len(nums):
            if two < one:
                nums[one], nums[two] = nums[two], nums[one]
                while two < len(nums) and nums[two] != 2:
                    two+=1
            else:
                one+=1
            while one < len(nums) and nums[one] != 1:
                one+=1
            
        
        
                
