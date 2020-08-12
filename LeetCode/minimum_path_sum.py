class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[0] * len(row) for row in grid]
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row - 1 < 0 and col -1 < 0:
                    memo[row][col] = grid[row][col]
                elif row - 1 < 0:
                    memo[row][col] = memo[row][col-1] + grid[row][col]
                elif col - 1 < 0:
                    memo[row][col] = memo[row-1][col] + grid[row][col]
                else:
                    memo[row][col] = min(memo[row-1][col], memo[row][col-1]) + grid[row][col]
                    
        return memo[-1][-1]
                
