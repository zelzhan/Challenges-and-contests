class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        
        row = [1, 1]
        i, j = 0, 1
        
        k = 1
        while k != rowIndex:
            i, j = 0, 1
            while j < len(row):
                row[i] = row[i] + row[j]
                i+=1
                j+=1
            row.insert(0, 1)
            k+=1
            
        
        return row
