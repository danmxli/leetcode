from collections import defaultdict
from typing import List

def reachableNodes(n: int, edges: List[List[int]], restricted: List[int]) -> int:
    restricted_set = set(restricted)
    graph = defaultdict(list)
    for edge in edges:
        if edge[0] in restricted_set or edge[1] in restricted_set:
            continue
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # dfs to find the number of reachable nodes
    seen = set()
    seen.add(0)

    def dfs(node: int):
        count = 1
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                count += dfs(neighbor)
        return count
    
    return dfs(0)

print(reachableNodes(n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]))