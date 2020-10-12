from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        invalids = [False] * len(transactions)
        
        table = defaultdict(list)
        for i, trans in enumerate(transactions):
            
            table[trans.split(",")[0]].append(i)
    
        for name, indexes in table.items():
            for i in range(len(indexes)):
                _, time1, price1, city1 = transactions[indexes[i]].split(",")
                if int(price1) > 1000:
                    invalids[indexes[i]] = True
         
                for j in range(i+1, len(indexes)):
                    
                    _, time2, price2, city2 = transactions[indexes[j]].split(",")

                    if abs(int(time1) - int(time2)) <= 60 and city1 != city2:
                        invalids[indexes[i]] = True
                        invalids[indexes[j]] = True
        
        res = []
        for i, invalid in enumerate(invalids):
            if invalid:
                res.append(transactions[i])
                
        return res
