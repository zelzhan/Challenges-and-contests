#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque, defaultdict

# Complete the bfs function below.
def bfs(n, m, edges, s):
    s -=1
    graph = defaultdict(set)
    for edge in edges:
        graph[edge[0]-1].add(edge[1]-1)
        graph[edge[1]-1].add(edge[0]-1)
    
    queue = deque()
    queue.append(s)
    visited = [False] * n
    distances = [0] * n
    visited[s] = True    
    while queue:
        node = queue.popleft()
        for adj in graph[node]:
            if not visited[adj]:
                queue.append(adj)
                distances[adj] = distances[node]+6
                visited[adj] = True
    
    for index, distance in enumerate(distances):
        if distance == 0:
            distances[index] = -1
    
    distances.pop(s)
    return distances
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
