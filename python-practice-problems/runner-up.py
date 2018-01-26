if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    arr.sort()
    counter = 0
    for i in arr:
        counter += 1        
    print(arr[counter-2])

