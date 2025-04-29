from typing import List
from collections import defaultdict, deque

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    
    if source == destination:
        return True

    D = defaultdict(list)
    for (u, v) in edges:
        D[u].append(v)
        D[v].append(u)

    seen = set()
    bfs_queue = deque()
    
    seen.add(source)
    bfs_queue.append(source)

    while bfs_queue:
        node = bfs_queue.popleft()
        
        for adj_node in D[node]:
            if adj_node == destination:
                return True
            if adj_node not in seen:
                seen.add(adj_node)
                bfs_queue.append(adj_node)

    return False


n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(validPath(n, edges, source, destination))