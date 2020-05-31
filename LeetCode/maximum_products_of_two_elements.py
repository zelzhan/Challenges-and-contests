import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        
        for i, num in enumerate(nums):
            heapq.heappush(heap, -num)
            
        
        return (heappop(heap)+1) * (heappop(heap)+1)
            
