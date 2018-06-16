def start():
    K = int(input())
    rooms = list(map(int, input().split(" ")))
    my_set = set(rooms)
    captain = (sum(my_set)*K - sum(rooms))/(K-1)
    print(int(captain))
    
    # for i in rooms:
        # if i in rooms: 
        #     rooms.remove(i)
        #     if i not in rooms: 
        #         print(i)
        #         return
        # if i in rooms:
        #     rooms = list(filter(lambda x: x!=i, rooms))

if __name__ == "__main__":
        start()
