from heapq import heappop, heappush
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        
        counter = Counter(s)
        
        heap = []
        for char, freq in counter.items():
            heappush(heap, (-freq, char))
            
        
        res = ""
        while heap:
            freq, char = heappop(heap)
            
            res += char * (-freq)
        
        return res
