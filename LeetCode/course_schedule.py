from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(set)
        for u, v in prerequisites:
            graph[v].add(u)
            graph[u]
            
        
        
        def dfs(numCourses):
            visited = [0] * numCourses
            
            def dfsUtil(node):
                
                # We found a backedge!
                if visited[node] == -1:
                    return False
                
                if visited[node] == 1:
                    return True
                
                visited[node] = -1
                for adj in graph[node]:
                    if not dfsUtil(adj):
                        return False
                
                visited[node] = 1
                return True
                
                
            for v in graph.keys():
                if not dfsUtil(v):
                    return False
            return True
        
        return dfs(numCourses)
            
            
