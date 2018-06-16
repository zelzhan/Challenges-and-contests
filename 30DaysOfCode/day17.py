class Calculator:
    def power(self, n, p):
        if (n<0 or p<0):
            raise Exception("n and p should be non-negative")
        x = n
        sum_=1
        for _ in range(p-1):
            n *= x
            sum_= n
        return sum_

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
