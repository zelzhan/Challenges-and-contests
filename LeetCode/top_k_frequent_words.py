from heapq import heappush, heappop
from collections import defaultdict
    
class Wrapper:
    def __init__(self, word, count):
        self.word = word
        self.count = count
            
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        else:
            return self.count < other.count
        
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word
    
class Solution(object):

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hashtable = defaultdict(int)
        for word in words:
            hashtable[word]+=1
            
        heap = []
        for key, value in hashtable.items():
            heappush(heap, Wrapper(key, value))
            if len(heap) > k:
                heappop(heap)
                
        res = []
        
        while heap:
            res.append(heappop(heap).word)
        
        res.reverse()
        return res
            
