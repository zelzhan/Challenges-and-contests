
'''Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.'''
class Solution:

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution 1 
        hashset = set()
        for num in nums:
            hashset.add(num)
            
        for i in range(len(nums)+1):
            if i not in hashset:
                return i
        return -1
    
        #solution 2
        sum_ = 0
        for num in nums:
            sum_+=num            
        return int((len(nums)+1)*((len(nums)/2) ) - sum_)

            
            
            
        
        
