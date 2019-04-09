class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) < 4 or len(s) > 12:
            return []
        
        def isValid(arr):
            if arr == '':
                return False
            if len(arr) > 1 and arr[0] == '0':
                return False
            value = int(arr)
            if 0 <= value <= 255:
                return True
            return False
        
        first, second, third = 1, 2, 3
        res = []
        while isValid(s[:first]) and first < second:
            second = first+1
            while isValid(s[first:second]) and second < third:
                third = second+1
                while isValid(s[second:third]) and third < len(s):
                    if isValid(s[third:]):
                        res.append(".".join([s[:first], s[first:second], s[second:third], s[third:]]))
                    third+=1                    
                second+=1
            first+=1
            
        return res
                            
