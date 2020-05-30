from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter = Counter(arr)
        for el in target:
            counter[el]-=1
            if counter[el] < 0:
                return False
            
        return True
        
