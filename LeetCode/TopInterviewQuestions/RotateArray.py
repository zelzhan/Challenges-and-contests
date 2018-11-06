'''Given an array, rotate the array to the right by k steps, where k is non-negative.'''

class Solution(object):
    def rotate_by_one(self, nums):
        if len(nums) <= 1: return
        temp = nums[0]
        for j in range(len(nums)-1, -1, -1):
            nums[(j + 1)%len(nums)] = nums[j]
        nums[1] = temp
 
    
            
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # nums = nums[k+1:len(nums)] + nums[0:k+1]  one line solution using slice
        
        
        # not efficient O(N^2) solution but with space complexity O(1)
        for i in range(k):
            self.rotate_by_one(nums)
            
