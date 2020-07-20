class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        stack = []
        res = []
        
        for i in range(len(T)-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                res.append(stack[-1] - i)
            else:
                res.append(0)
            stack.append(i)
    
        return res[::-1]
                
                
            
