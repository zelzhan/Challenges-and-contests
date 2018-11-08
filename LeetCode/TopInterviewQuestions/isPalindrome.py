'''Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.'''
class Solution:
    
    
    def leftAlpha(self, left, s):
        for i in range(left, len(s)):
            if s[i].isalnum():
                return i+1, s[i].lower() 
        return 0, ""
    def rightAlpha(self, right, s):
        for i in range(right, -1, -1):
            if s[i].isalnum():
                return i-1, s[i].lower()
        return 0, ""
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        left = 0
        right = len(s) - 1
        temp1, temp2 = "", ""
        
        while right - left > 0:
            left, temp1 = self.leftAlpha(left, s)
            right, temp2 = self.rightAlpha(right, s)
            
            print(temp1, temp2)
            if temp1 != temp2:
                return False
            
        return True
