from typing import List
from collections import defaultdict

# intuition:
# - build the graph
# - dfs from city 0
# - count the number of edges that need to be reversed

def minReorder(n: int, connections: List[List[int]]) -> int:
    # build the graph
    graph = defaultdict(list)
    for src, dst in connections:
        graph[src].append((dst, 1))
        graph[dst].append((src, 0))
    
    # dfs
    visited = set()
    count = [0]
    def dfs(city: int):
        ...
        visited.add(city)
        for adj, weight in graph[city]:
            if adj not in visited:
                count[0] += weight
                dfs(adj)
    
    # driver
    dfs(0)
    return count[0]

print(minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))