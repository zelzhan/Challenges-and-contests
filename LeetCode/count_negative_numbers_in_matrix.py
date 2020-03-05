class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        counter = 0
        for row in grid:
            for i in range(len(row)-1, -1, -1):
                if row[i] >= 0 or (i == 0 and row[i] >= 0):
                    break
                counter+=1
        
        return counter
