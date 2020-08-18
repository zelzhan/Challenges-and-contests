class Solution:
    def numSquares(self, n: int) -> int:
       
        queue = [(n, 0)]
        
        visited = set()
        
        level = 0
        
        while queue:
            n, level = queue.pop(0)
            if n == 0:
                return level
            
            upper_base = int(n**(1/2))
            while upper_base > 0:
                if n-(upper_base**2) not in visited:
                    queue.append((n-(upper_base**2), level+1))
                    visited.add((n-(upper_base**2)))
                upper_base-=1
    
        return level 
        
