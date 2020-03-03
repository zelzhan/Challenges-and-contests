class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            row.reverse()
            
        
        for row in A:
            for i, el in enumerate(row):
                if el == 1:
                    row[i] = 0
                else:
                    row[i] = 1
                    
                
        return A
