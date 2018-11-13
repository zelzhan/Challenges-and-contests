'''Given two arrays, write a function to compute their intersection.'''
from collections import defaultdict

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        hashtable = defaultdict(int)
        if len(nums1) > len(nums2):
            for num in nums1:
                hashtable[num]+=1
            for num in nums2:
                if hashtable[num] != 0:
                    res.append(num)
                    hashtable[num]-=1
        else:
            for num in nums2:
                hashtable[num]+=1
            for num in nums1:
                if hashtable[num] != 0:
                    res.append(num)
                    hashtable[num]-=1
        return res
        
# follow-up
from collections import defaultdict
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums2) > len(nums1): 
            nums1, nums2 = nums2, nums1
            
        hashtable1 = defaultdict(int)
        for num in nums1:
            hashtable1[num]+=1
        res = []
        for num in nums2:
            if num in hashtable1:
                res.append(num)
                hashtable1[num]-=1
                if hashtable1[num] == 0:
                    del hashtable1[num]
            
        
        return res
