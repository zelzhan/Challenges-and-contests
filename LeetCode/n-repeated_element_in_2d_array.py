class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        table = set()
        
        for el in A:
            if el in table:
                return el
            table.add(el)
            
        return None
