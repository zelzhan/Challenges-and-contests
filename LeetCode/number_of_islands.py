class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        def DFS():
            counter = 0
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == "1":
                        counter+=1
                        DFSUtil(row, col)
            return counter
                    
        def check_boundaries(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
                    
        
        def DFSUtil(row, col):
            if grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
            
            
            for i, j in directions:
                if check_boundaries(row+i, col+j):
                    DFSUtil(row+i, col+j)
            
            
        
        return DFS()
