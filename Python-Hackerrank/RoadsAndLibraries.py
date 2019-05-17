#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return c_lib * n

    graph = defaultdict(set)
    for road in cities:
        graph[road[0]].add(road[1])
        graph[road[1]].add(road[0])
    
    trees = dfs(graph, n)
    res = 0
    for tree in trees:
        res+=(tree-1)*c_road
    res+=len(trees)*c_lib
    return res

def dfs_util(city, graph, visited, nodes):
    print(city)
    if not visited[city]:
        nodes[0]+=1
        visited[city] = True
        for adjacent in graph[city]:
            dfs_util(adjacent, graph, visited, nodes)

def dfs(graph, n):
    visited = {value:False for value in range(1, n+1)}
    trees = []
    for city in range(1, n+1):
        nodes = [0]
        dfs_util(city, graph, visited, nodes)
        if nodes[0]:
            trees.append(*nodes)
    return trees



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
