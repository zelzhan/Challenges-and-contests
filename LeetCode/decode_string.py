class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        
        cur = ""
        stack = []
        num = 0
        for c in s:
            if c == '[':
                stack.append(cur)
                stack.append(num)
                cur = ""
                num = 0
            elif c.isnumeric():
                num = num*10 + int(c)
            elif c == ']':
                popped = stack.pop()
                cur = stack.pop() + popped * cur
            else:
                cur = cur + c
        
        return cur
        
