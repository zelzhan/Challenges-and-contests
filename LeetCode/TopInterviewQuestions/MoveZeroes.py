'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.'''

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pointer = len(nums)
        for i in range(len(nums)):
            if nums[i] == 0 and i < pointer:
                pointer = i
            elif pointer != len(nums) and nums[i] != 0:
                nums[pointer] = nums[i]
                nums[i] = 0
                pointer+=1
