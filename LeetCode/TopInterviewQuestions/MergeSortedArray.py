'''Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        tail1 = -1
        tail2 = -1
        while m != 0 and nums2:
            if nums1[m-1] > nums2[tail2]:
                nums1[tail1] = nums1[m-1]
                nums1[m-1] = 0
                m-=1
            else:
                nums1[tail1] = nums2.pop()
            tail1-=1
        for i in range(len(nums2)):
            nums1[i] = nums2[i]
        
        
        
            
            
