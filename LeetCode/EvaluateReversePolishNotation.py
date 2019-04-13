class Solution(object):
    def evalRPN(self, tokens):
        if not tokens:
            return 0
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = ("+", "-", "/", "*")
        
        def op(n, arg1, arg2):
            
            if n == 0:
                return int(arg1)+int(arg2)
            elif n == 1:
                return int(arg1)-int(arg2)
            elif n == 2:
                return int(arg1/arg2)
            elif n == 3:
                return int(arg1)*int(arg2)
            else:
                raise Exception("Wrong input")
        
        tokens = tokens[::-1]
        res = tokens[0]
        stack = []
        while tokens:
            token = tokens.pop()
            if token in operations:
                int2 = float(stack.pop())
                int1 = float(stack.pop())
                res = op(operations.index(token), int1, int2)
                stack.append(res)
            else:
                stack.append(token)
        return res
                
                
