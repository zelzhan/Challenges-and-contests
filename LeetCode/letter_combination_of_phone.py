class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz")
        }
        
        def comb(digits):
            
            if not digits:
                return []
            
            if len(digits) == 1:
                return [[digit] for digit in phone[digits]]
            
            res = []
            for com in comb(digits[1:]):
                for letter in phone[digits[0]]:
                    res.append([letter] + com)
                    
            return res
        
        
        return ["".join(l) for l in comb(digits)]
