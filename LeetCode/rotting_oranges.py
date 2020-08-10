class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        
        fresh = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rotten.add((row, col, 0))
                elif grid[row][col] == 1:
                    fresh.add((row, col))
                    
        if not fresh:
            return 0
        queue = list(rotten)
                    
        def MultiBFS():
            max_level = -1
            while queue:
                row, col, level = queue.pop(0)
                if level > max_level:
                    max_level = level
                if row + 1 < len(grid) and (row+1,  col) in fresh:
                    fresh.remove((row+1, col))
                    queue.append((row+1, col, level+1))
                if row - 1 >= 0 and (row-1, col) in fresh:
                    fresh.remove((row-1, col))
                    queue.append((row-1, col, level+1))
                if col + 1 < len(grid[0]) and (row, col+1) in fresh:
                    fresh.remove((row, col+1))
                    queue.append((row, col+1, level+1))
                if col - 1 >= 0 and (row, col-1) in fresh:
                    fresh.remove((row, col-1))
                    queue.append((row, col-1, level+1))
                    
            return max_level
        
        level = MultiBFS()
        if fresh:
            return -1
        return level
                
            
            
        
