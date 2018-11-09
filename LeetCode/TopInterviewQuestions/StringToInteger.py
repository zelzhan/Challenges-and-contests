'''Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.'''

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        temp = 0
        result = 0
        started = False
        for s in str:
            # print(not s.isnumeric(), 
            if s == '-' and temp == 0 and not started:
                started = True
                temp = -1
            elif s == '+' and temp == 0 and not started:
                started = True
                temp = +1
            elif s.isnumeric():
                started = True
                result*=10
                result += int(s)
            elif not s.isnumeric() and started:
                
                
                if temp != 0: result *=temp
                
                if result > 2**31 - 1:
                    return 2**31 - 1
                elif result < -2**31:
                    return -2**31
                
                return result
            elif not s.isnumeric() and s != " " and not started:
                return 0
        
        if temp != 0: result *=temp
        
        if result > 2**31 - 1:
            return 2**31 - 1
        elif result < -2**31:
            return -2**31
        return result
            
        
