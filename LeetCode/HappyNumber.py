from collections import defaultdict 
class Solution:
    def isHappy(self, n: int) -> bool:
        hashtable = defaultdict(int)
        while True:
            summ = 0
            while n!=0:
                summ+=(n%10)**2
                n = n//10
            if summ == 1:
                return True
            elif hashtable[summ] != 0:
                return False
            hashtable[summ]+=1
            n = summ
