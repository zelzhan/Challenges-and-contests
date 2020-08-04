class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # 7 2 3
        # 8 5 6
        # 9 4 1
        
        matrix.reverse()
        
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
