from typing import List
from collections import deque

def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    M = len(isWater)
    N = len(isWater[0])


    def bfs(nodes: List[set], visited: List[List[bool]]):
        queue = deque(nodes)

        while queue:
            curr = queue.popleft()
            for d in [(-1,0),(1,0),(0,-1),(0,1)]:
                adj_i = curr[0] + d[0]
                adj_j = curr[1] + d[1]

                if not(0 <= adj_i < M) or not(0 <= adj_j < N):
                    continue
                if visited[adj_i][adj_j]:
                    continue
                
                # update height
                answer[adj_i][adj_j] = answer[curr[0]][curr[1]] + 1
                visited[adj_i][adj_j] = True
                queue.append((adj_i, adj_j))

    # answer matrix
    answer = [[0] * N for _ in range(M)]
    # boolean matrix to track visited nodes
    visited = [[False] * N for _ in range(M)]

    # find all water nodes
    water_nodes = []
    for i in range(M):
        for j in range(N):
            if isWater[i][j] == 1:
                visited[i][j] = True
                water_nodes.append((i,j))

    bfs(water_nodes, visited)    
    return answer

print(highestPeak([[0,0],[1,1],[1,0]]))