from collections import defaultdict
import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # step1: state recurrence relation:
        # f(X) = min(f(X-C[i])) + 1, where C is array of coins
        
        # step2: write the base case:
        # f(0) = 0
        
        # step3: write the recursively/iteratevely the function
    
        memo = defaultdict(int)
        
        def dp(coins, amount):

            #base case:
            if amount == 0:
                return 0
            elif amount < 0:
                return -1
            
            if amount in memo:
                return memo[amount]
            else:
                min_val = sys.maxsize

                for coin in coins:
                    res = dp(coins, amount-coin) + 1
                    if res == 0:
                        continue
                    elif  res < min_val:
                        min_val = res
                
                
                memo[amount] = min_val
            if min_val == sys.maxsize:
                return -1
            return min_val
        
        return dp(coins, amount)
                
            
        
