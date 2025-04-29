from typing import List
from collections import deque, defaultdict
import math

def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    ...
    D = defaultdict(list)
    for (u,v) in redEdges:
        D[u].append((v, True)) # node, is_red
    for (u,v) in blueEdges:
        D[u].append((v, False))
    

    answer = [-1] * n
    answer[0] = 0
    # init with both red and blue
    queue = deque([(0, True), (0, False)])
    visited = set([(0, True), (0, False)])
    distance = -1

    while queue:
        distance += 1
        for _ in range(len(queue)):
            curr_n, curr_b = queue.popleft()
            # update answer array
            if answer[curr_n] == -1:
                answer[curr_n] = distance
            else:
                answer[curr_n] = min(answer[curr_n], distance)

            for adj_n, adj_b in D[curr_n]:
                if curr_b == adj_b:
                    continue
                if (adj_n, adj_b) in visited:
                    continue
                visited.add((adj_n, adj_b))
                queue.append((adj_n, adj_b))
    
    return answer

print(shortestAlternatingPaths(n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]))