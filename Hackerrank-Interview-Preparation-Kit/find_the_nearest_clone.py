#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
from collections import defaultdict, deque

def define_graph(graph_nodes, graph_from, graph_to, ids, val):
    graph = defaultdict(list)
    for i in range(len(graph_from)):
        
        if not graph[graph_from[i]]:
            color = ids[graph_from[i]-1]
            graph[graph_from[i]] = [[graph_to[i]], color]
        else:
            graph[graph_from[i]][0].append(graph_to[i])

        
        if not graph[graph_to[i]]:
            color = ids[graph_to[i]-1]
            graph[graph_to[i]] = [[graph_from[i]], color] 
        else:
            graph[graph_to[i]][0].append(graph_from[i])

    return graph


def bfs(graph_nodes, graph, start_node, color):
    queue = deque()
    visited = [-1] * (graph_nodes + 1)
    visited[start_node] = 0
    queue.append(start_node)
    while queue:
        node = queue.popleft()
        adj, col = graph[node]
        if col == color and node != start_node:
            return visited[node]

        for edge in adj:
            if visited[edge] < 0:
                queue.append(edge)
                visited[edge] = visited[node] + 1
        print(visited)

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = define_graph(graph_nodes, graph_from, graph_to, ids, val)
    minim = sys.maxsize

    nodes = graph.keys()
    for node in nodes:
        if graph[node][1] == val:
            res = bfs(graph_nodes, graph, node, val)
            if not res:
                return -1
            if res < minim:
                minim = res            

    if minim == sys.maxsize:
        return -1
    return minim

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
