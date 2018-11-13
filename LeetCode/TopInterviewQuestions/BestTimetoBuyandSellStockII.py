'''Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) == 0: return 0
        buy, sell = True, False
        minim, maxim = prices[0], prices[0]
        result = 0
        for i in range(len(prices)):
            if i+1 == len(prices): break
            if prices[i+1] > prices[i] and buy:
                buy = False
                sell = True
                minim = prices[i]
            elif prices[i+1] < prices[i] and sell:
                sell = False
                maxim = prices[i]
                
            if len(prices) == i+2 and sell:
                sell = False
                maxim = prices[i+1]

            if not sell and not buy:
                result += maxim - minim
                buy = True
                
        return result

    #=================================
    # Follow-up
    class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(prices)):
            if i + 1 == len(prices):
                break
            if prices[i+1]>prices[i]:
                res+=prices[i+1] - prices[i]
        return res
            
