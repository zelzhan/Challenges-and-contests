'''Given a non-empty array of integers, every element appears twice except for one. Find that single one.'''

from collections import defaultdict

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hashTable = defaultdict(int)
        for num in nums:
            hashTable[num]+=1
        for num in nums:
            if hashTable[num] == 1:
                return num 
                
        
