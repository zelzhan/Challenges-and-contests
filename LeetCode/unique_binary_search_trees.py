class Solution:
    def numTrees(self, n: int) -> int:
        
        
        
        memo = {0: 1, 1: 1}
        
        def countTrees(num):
            
            if num in memo:
                return memo[num]
            
            res = 0
            
            for i in range(num):
                res+=countTrees(i) * countTrees(num-i-1)

            
            memo[num] = res
            return res
        
        return countTrees(n)
        
