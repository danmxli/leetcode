from typing import List
from collections import defaultdict, deque

def topological_sort(condition_graph: List[List[int]], k: int) -> List[int]:
    D = defaultdict(list, {node: [] for node in range(1, k+1)})
    for (u,v) in condition_graph:
        D[u].append(v)

    in_degree = [0] * (k+1)
    for node in range(1, k+1):
        for adj_node in D[node]:
            in_degree[adj_node] += 1
    
    queue = deque()
    for node in range(1, k+1):
        if in_degree[node] == 0:
            queue.append(node)
    
    ordering = []
    while queue:
        node = queue.popleft()
        ordering.append(node)
        for adj_node in D[node]:
            in_degree[adj_node] -= 1
            if in_degree[adj_node] == 0:
                queue.append(adj_node)
    
    if len(ordering) != k:
        return []
    return ordering

def buildMatrix(k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
    ...
    row_ordering = topological_sort(rowConditions, k)
    col_ordering = topological_sort(colConditions, k)

    if not row_ordering or not col_ordering:
        return []

    row_map = {row_ordering[i]: i for i in range(k)}
    col_map = {col_ordering[i]: i for i in range(k)}

    matrix = [[0] * k for _ in range(k)]
    for i in range(1, k+1):
        matrix[row_map[i]][col_map[i]] = i
    return matrix

print(buildMatrix(3, [[1,2],[3,2]], [[2,1],[3,2]]))