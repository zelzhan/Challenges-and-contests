class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        nums = [len(str(n)) for n in nums]
        counter = 0
        for num in nums:
            if num%2==0:
                counter+=1
        
        return counter
