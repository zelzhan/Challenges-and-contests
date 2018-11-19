'''We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.'''

from collections import deque
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        bits = deque(bits)
        while bits:
            temp = bits.popleft()
            if not bits:
                return True
            if temp == 1:
                bits.popleft()
        return False
        
        
