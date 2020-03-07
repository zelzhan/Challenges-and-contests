import math
class Solution:
    def maximum69Number (self, num: int) -> int:
        
        num = str(num)
        res = 0
        mult = len(num) - 1
        found = False
        for el in num:
            if not found and el == "6":
                res+=9*(10**mult)
                found = True
            else:
                res+=int(el)*(10**mult)
            mult-=1
        
        return res
