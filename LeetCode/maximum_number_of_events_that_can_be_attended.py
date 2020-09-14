from heapq import heapify, heappop
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        events.sort(key=lambda x: x[0])
        
        events.reverse()
                
        heap = []
        
        res = 0
        i = 1
        while heap or events:
            while events and events[-1][0] == i:
                heappush(heap, events.pop()[1])
            
            correct = False
            while heap:
                if heappop(heap) >= i:
                    correct = True
                    break
            
            if correct:
                res+=1
            i+=1
            
        return res
                    
    
        
