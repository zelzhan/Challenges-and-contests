class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        def checkPalindrome(s, left, right):
            result = []
            while left>=0 and right < len(s):
                if s[left] != s[right]:
                    return result
                elif left == right:
                    result.append(s[left])
                else:
                    result.insert(0, s[left])
                    result.append(s[right])
                left-=1
                right+=1
            return result
        res = []
        for i in range(len(s)-1):
            palindrome1 = checkPalindrome(s, i, i)
            palindrome2 = checkPalindrome(s, i, i+1)
            if len(palindrome1) > len(palindrome2) and len(palindrome1) > len(res):
                res = palindrome1
            elif len(palindrome2) > len(res):
                res = palindrome2
        return "".join(res)
            
            
