from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        
        path_exists = set()
        
        for u, v in connections:
            path_exists.add((u, v))
        
        def DFS():    
            visited = [False] * n
            return DFSUtil(0, visited)
            
        def DFSUtil(v, visited):
            
            visited[v] = True
            counter = 0
            dfs_res_counter = 0
            for adj in graph[v]:
                if not visited[adj]:
                    if (adj, v) not in path_exists:
                        counter+=1
                    dfs_res_counter+=DFSUtil(adj, visited)
            return counter+dfs_res_counter
                    
        return DFS()
            
        
