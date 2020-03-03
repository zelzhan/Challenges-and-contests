class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def self_divisible(num):
            orig = num
            while num:
                digit = num%10
                if digit == 0 or not orig%digit == 0:
                    return False
                num//=10
                
            return True
        
        
        res = []
        for num in range(left, right+1):
            if self_divisible(num):
                res.append(num)
        
        return res
