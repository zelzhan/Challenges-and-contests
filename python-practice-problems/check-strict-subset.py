def start():
    A = list(map(int, input().split(" ")))
    N = int(input())
    list_ = []
    for i in range(N):
        temp = list(map(int, input().split(" ")))
        list_.append(temp)
    for i in range(N):
        for j in list_[i]:
            if j not in A: 
                print("False")
                return
        if len(list_[i]) == len(A): 
            print("False")
            return 
    print("True")



if __name__ == "__main__":
    start()
