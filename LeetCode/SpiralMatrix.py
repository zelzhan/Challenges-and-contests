'''Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        row = len(matrix)
        lowcolumn, lowrow = 0, 0
        column = len(matrix[0])
        length = len(matrix) * len(matrix[0])
        
        right, down, left, up = True, False, False, False
        res = []
        while True:
            if right:
                for i in range(lowcolumn, column):
                    print(matrix[lowrow][i], lowrow, i)
                    res.append(matrix[lowrow][i])
                    length -=1
                if length == 0: break
                lowrow+=1
                right = False
                down = True
            elif down:
                for i in range(lowrow, row):
                    res.append(matrix[i][column-1])
                    length-=1
                if length == 0: break
                column-=1
                down = False
                left = True
            elif left:
                for i in range(column-1, lowcolumn-1, -1):
                    res.append(matrix[row-1][i])
                    length-=1
                if length == 0: break
                row-=1
                left = False
                up = True
            elif up:
                for i in range(row-1, lowrow-1, -1):
                    res.append(matrix[i][lowcolumn])
                    length-=1
                if length == 0: break
                lowcolumn+=1
                up = False
                right = True
        return res
                    
