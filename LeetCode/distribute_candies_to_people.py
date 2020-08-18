class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        num = 1
        i = 0
        while candies:
            if candies-num <= 0:
                res[i]+=candies
                break
            res[i] += num
            candies-=num
            
            num+=1
            i+=1
            if i == len(res):
                i = 0
        return res
            
