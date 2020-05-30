import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            distance = (x**2 + y**2)**(1/2)
            heapq.heappush(heap, (distance, [x, y]))
        
        res = []
        while K:
            _, point = heapq.heappop(heap)
            res.append(point)
            K-=1
            
        return res
        
