import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
            
        # 7 1 5 3 -1 6 4
        # index = 4         < 7
        # minim = 1
        # diff = 4
        minim = prices[0]
        diff = 0
        index = 1
        while index < len(prices):
            if prices[index] > prices[index-1]:
                if prices[index-1] < minim:
                    minim = prices[index-1]
            temp = prices[index] - minim
            if temp > diff:
                diff = temp
            index+=1
        return diff
