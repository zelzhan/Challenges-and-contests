class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        if not prices:
            return 0
        
        s0 = [0] * len(prices)
        s1 = [-prices[0]] * len(prices)
        s2 = [-100000] * len(prices)
        
        for i in range(1, len(prices)):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            s2[i] = s1[i-1] + prices[i]
        
        return max(s0[-1], s2[-1])
            
