import sys
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        table = {}
        
        for i, rest in enumerate(list1):
            table[rest] = i
            
        _min = sys.maxsize
        for j, rest in enumerate(list2):
            if rest in table and j + table[rest] < _min:
                _min = j + table[rest]
                
        
        res = []
        for j, rest in enumerate(list2):
            if rest in table and j + table[rest] == _min:
                res.append(rest)
                
        return res
