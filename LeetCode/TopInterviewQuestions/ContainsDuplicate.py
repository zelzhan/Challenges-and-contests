'''Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.'''

from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
    
        """
        dictionary = defaultdict(int)
        
        if len(nums) <= 1: return False   
            
        for i in range(len(nums)):
            dictionary
            if dictionary[nums[i]] == 1:
                return True
            else:
                dictionary[nums[i]] = 1
        return False
        
# follow-up
from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashset = defaultdict(int)
        for i in range(len(nums)):
            hashset[nums[i]] = i
            
        for j in range(len(nums)):
            temp = target-nums[j]
            if temp in hashset and j != hashset[target-nums[j]]:
                return [j, hashset[target-nums[j]]]
        
