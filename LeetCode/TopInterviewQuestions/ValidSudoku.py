'''Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''
class Solution:
    
    def parseSquare(self, board, low1, up1, low2, up2):
        set1 = set()
        for i in range(low1,up1):
            for k in range(low2,up2):
                if board[i][k] in set1:
                    return False
                elif board[i][k] !=".":
                    set1.add(board[i][k])
        return True
                
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        set2 = set()
        for i in range(9): 
            set1 = set()
            set3 = set()
            
            for f in range(9):
                if board[f][i] in set3:
                    return False
                elif board[f][i] != ".":
                    set3.add(board[f][i])
            
            for j in range(9):
                if board[i][j] in set1:
                    return False
                elif board[i][j] != ".":
                    set1.add(board[i][j])
            
        low1 = 0
        up1 = 3
        low2 = 0
        up2 = 3
        for k in range(9):
            boolean = self.parseSquare(board, low1, up1, low2, up2)
            if not boolean: return False
            low1+=3
            up1+=3
            if low1 == 9:
                low1 = 0
                up1 = 3
                low2 +=3
                up2 +=3
        return True
