class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mult, summ = 1, 0
        while n:
            digit = n%10
            mult*=digit
            summ+=digit
            n//=10
            
        return mult-summ
