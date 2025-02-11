from typing import List
from collections import deque
import heapq

def trapRainWater(heightMap: List[List[int]]) -> int:
    M = len(heightMap)
    N = len(heightMap[0])

    # init min priority queue with bordering nodes, and visited set
    pq = []
    visited = set()
    for i in range(M):
        for j in range(N):
            if i == 0 or i == M-1 or j == 0 or j == N-1:
                heapq.heappush(pq, (heightMap[i][j], i,j))
                visited.add((i,j))

    answer = 0
    max_height = -1
    
    # bfs
    while pq:
        ...
        curr_height, curr_i, curr_j = heapq.heappop(pq)
        max_height = max(max_height, curr_height)
        answer += max_height - curr_height

        # neighbor exploration, prioritize minimum heights
        for d in [(-1,0), (1,0), (0,-1), (0,1)]:
            adj_i = curr_i + d[0]
            adj_j = curr_j + d[1]

            if (adj_i, adj_j) in visited:
                continue
            if not(0 <= adj_i < M) or not(0 <= adj_j < N):
                continue

            heapq.heappush(pq, (heightMap[adj_i][adj_j], adj_i, adj_j))
            visited.add((adj_i, adj_j))
                
    return answer


print(trapRainWater(heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))