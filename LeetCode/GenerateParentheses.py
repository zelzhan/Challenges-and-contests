class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # (())()
        if not n:
            return []
        def helper(string, num_opening, num_closing):
            if num_opening == 0:
                return [string + ')' * num_closing]
            elif num_closing == 0:
                return helper(string + '(', num_opening-1, num_closing+1 )
            else:
                return helper(
                    string + '(', num_opening-1, num_closing+1
                ) + helper(
                    string + ')', num_opening, num_closing-1
                )
            
            
        return helper("", n, 0)
            
    
        
        
        
