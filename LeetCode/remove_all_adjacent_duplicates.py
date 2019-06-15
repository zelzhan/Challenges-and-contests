class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """

        # edge cases:
        # 1) empty string = pass
        # 2) 1/2 chars in the string = pass 
        # 3) all chars are the same = pass
        
        # a a a 
        # [ 
        
        s = list(S)
        stack = []
        i = 0
        while i < len(s):
            
            # check is stack is empty
            if not stack:
                stack.append(s[i])
                i+=1
                continue

            # remove all adjacent duplicates
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
            
            i+=1
            
        return "".join(stack)
            
