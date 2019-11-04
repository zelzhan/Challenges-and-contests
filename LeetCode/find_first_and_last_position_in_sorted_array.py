class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            mid = left + (right - left)//2 
            print(mid)
            while left <= right:
                if target > nums[mid]:
                    left = mid + 1
                    mid = left + (right - left)//2
                elif target < nums[mid]:
                    right = mid - 1
                    mid = left + (right - left)//2
                else:
                    return mid
            return -1
        
        
        index = binary_search(nums, target)
        
        if index < 0 :
            return [-1, -1]
        
        right, left = index, index
        
        while right + 1 < len(nums) and nums[right+1] == nums[right]:
            right+=1
        
        while left - 1 >= 0 and nums[left - 1] == nums[left]:
            left-=1
            
        return [left, right]
        
        
