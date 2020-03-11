class Solution:
    def fib(self, N: int) -> int:
        
        memo = [0, 1]
        
        def fib(num):
            if num < len(memo):
                return memo[num]
            
            
            memo.append(fib(num-1) + fib(num-2)) 
            return memo[num]
        
        
        return fib(N)
        
