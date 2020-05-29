from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for u, v in prerequisites:
            graph[u].append(v)
            
        
        def DFSUtil(course, visited=set()):
            
            if course in visited:
                return True
            
            visited.add(course)
            
            for adj in graph[course]:
                if DFSUtil(adj, visited):
                    return True
            
            visited.remove(course)
            return False
            
        
        def DFS():
            for course in range(numCourses):
                if DFSUtil(course):
                    return False
            
            return True
        
        
        return DFS()
                
            
        
                
        
        
