'''You are given three integers: a, b, and m, respectively. Print two lines. 
The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).'''

def start():
    a, b, m = int(input()), int(input()), int(input())
    print(pow(a, b))
    print(pow(a, b, m))
    
if __name__ == "__main__":
    start()
