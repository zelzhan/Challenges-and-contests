import heapq
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        heap = []
        
        for i, cost in enumerate(costs):
            
            heappush(heap, (cost[0]-cost[1], i))
        
        res = 0
        
        N = len(costs)//2
        
        for i in range(N):
            _, index = heappop(heap)
            res += costs[index][0]
        
        
        while heap:
            _, index = heappop(heap)
            res += costs[index][1]
        
        return res
        
