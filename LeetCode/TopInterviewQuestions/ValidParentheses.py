'''Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "": return True
        stack = []
        matching = {'{': '}', '}':'{',  '(':')',  ')':'(',  '[':']',  ']':'['}

        temp1 = ""
        for c in s[::-1]:
            if stack:
                temp1 = stack.pop()
            if matching[c] == temp1:
                continue
            stack.append(temp1)
            stack.append(c)
        if len(stack) == 1:
            return True
        return False
