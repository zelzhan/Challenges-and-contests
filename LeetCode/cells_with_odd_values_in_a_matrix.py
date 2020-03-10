class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        mat = [[0 for _ in range(m)] for _ in range(n)]
        
        for row, column in indices:
            for i in range(m):
                mat[row][i] += 1
            
            for j in range(n):
                mat[j][column] += 1
        
        counter = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]%2!=0:
                    counter+=1
        
        return counter
