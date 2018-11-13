'''Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.'''

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits)-1]+=1
        for i in range(len(digits)-1, -1, -1):
            if i-1 < 0 and digits[i]//10 != 0:
                digits.insert(0, digits[i]//10)
                digits[i+1] = digits[i+1]%10
            elif digits[i] >= 10:
                digits[i-1] = digits[i-1] + digits[i]//10                
                digits[i] = digits[i]%10
        return digits
# follow-up
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1]+=1
        temp = 0
        for i in range(len(digits)-1, -1, -1):
            digits[i]+=temp
            temp = digits[i]//10
            digits[i] = digits[i]%10
            if temp == 0:
                break
        if temp != 0:
            digits.insert(0, 1)
        return digits
