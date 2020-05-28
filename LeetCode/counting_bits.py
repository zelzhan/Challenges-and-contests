class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]
        
        power = 0
        
        for i in range(1, num+1):
            if i == 2**power:
                
                dp.append(1)
                power+=1
            else:
                dp.append(1 + dp[i%(2**(power-1))])
                
        return dp
