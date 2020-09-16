class Solution:
    def numberToWords(self, num: int) -> str:
        
        if not num:
            return "Zero"
        
        digits = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }
        
        
        exceptions = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }
        
        tens = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        
        def getHundreds(number):
            
            res = []
            if number%100 in exceptions:
                res.append(exceptions[number%100])
                number//=100
            else:
                if number%10 in digits:
                    res.append(digits[number%10])
                number//=10
                if number%10 in tens:
                    res.append(tens[number%10])
                number//=10
            
            if number in digits:
                res.append("Hundred")
                res.append(digits[number])
            
            return " ".join(reversed(res)).strip()
        
        
        res = []
        
        res.append(getHundreds(num%1000))
        
        num//=1000
        
        if not num:
            return "".join(res).strip()
        
        
        if num%1000 != 0:
            res.append("Thousand")
            res.append(getHundreds(num%1000))
        
        
        num//=1000
        
        if not num:
            return " ".join(reversed(res)).strip()
        
        if num%1000 != 0:
            res.append("Million")
            res.append(getHundreds(num%1000))
        
        num//=1000
        
        if not num:
            return " ".join(reversed(res)).strip()
        
        res.append("Billion")
        res.append(getHundreds(num%1000))
        
        return " ".join(reversed(res)).strip()
        
