from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:
        table = defaultdict(int)
        
        table[0]+=1
            
        cur = 0
        res = 0
        
        for num in nums:
            cur+=num
            res+=table[cur-target]
            table[cur]+=1
            
            
        return res
            
        
        
    
    
