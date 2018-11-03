'''Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0: return 0
        
        length, i = 1, 0
        while i+1 != len(nums):
            if nums[i] != nums[i+1]:
                length+=1
                i+=1
            else:
                del nums[i]
        return length
        
