def start():
    N = int(input())
    for i in range(N):
        m = input()
        A = list(map(int , input().split(" ")))
        b = input()
        B = list(map(int , input().split(" ")))
        for i in A:
            if i not in B:
                print("False")
                break
            if i == A[-1]: print("True")
                

if __name__ == "__main__":
    start()
