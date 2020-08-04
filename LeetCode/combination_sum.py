from collections import defaultdict
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # 2 3 6 7
        
        # 2 : [2]
        # 3 : [3]
        # 4 : [2, 2]
        # 5 : [2, 3]
        # 6 : [2, 2, 2], [3, 3]
        
        candidates.sort()
        
        def traverse(cur, comb, i):
            
            if cur == target:
                res.append(comb)
                return
            
            for j in range(i, len(candidates)):
                if cur + candidates[j] > target:
                    break
                traverse(cur + candidates[j], comb + [candidates[j]], j)
        
        res = []
        traverse(0, [], 0)
        
        return res
