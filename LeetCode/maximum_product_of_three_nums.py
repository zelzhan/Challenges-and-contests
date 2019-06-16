import sys
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxim1 = -sys.maxsize
        maxim2 = maxim3 = maxim1
        minim1, minim2 = sys.maxsize, sys.maxsize
        for num in nums:
            if num < minim2:
                minim2 = num
                if minim2 < minim1:
                    temp = minim2
                    minim2 = minim1
                    minim1 = temp
            if num > maxim3:
                maxim3 = num
                if maxim3 > maxim2:
                    temp = maxim2
                    maxim2 = maxim3
                    maxim3 = temp
                
                if maxim2 > maxim1:
                    temp = maxim2
                    maxim2 = maxim1
                    maxim1 = temp
    
    
        return max(maxim1*maxim2*maxim3, maxim1 * minim1 * minim2)
