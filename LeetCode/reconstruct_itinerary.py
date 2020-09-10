from collections import defaultdict
from heapq import heappop, heappush, heapify
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        
        for u in graph.keys():
            heapify(graph[u])
        
        path = []
        def dfs(node):
            
            
            while graph[node]:
                adj = heappop(graph[node])
                dfs(adj)
            path.append(node)
        
        dfs("JFK")
        return path[::-1]
            
        
        
        
