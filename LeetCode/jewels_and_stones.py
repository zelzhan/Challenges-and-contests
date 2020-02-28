class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        counter = 0
        for el in S:
            if el in jewels:
                counter+=1
        return counter
            
