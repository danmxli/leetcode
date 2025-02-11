from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        if grid[0][0] == 1 or grid[M-1][N-1] == 1:
            return -1

        # bfs
        queue = deque()
        visited = set()
        # init
        queue.append((0,0))
        visited.add((0,0))
        level = 0

        while queue:
            level += 1

            for _ in range(len(queue)):
                curr_i, curr_j = queue.popleft()

                if curr_i == M-1 and curr_j == N-1:
                    return level
                
                # 8-directional exploration
                for d in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]:
                    adj_i = curr_i + d[0]
                    adj_j = curr_j + d[1]

                    if (adj_i, adj_j) in visited:
                        continue
                    if not(0 <= adj_i < M) or not(0 <= adj_j < N):
                        continue
                    if grid[adj_i][adj_j] == 1:
                        continue

                    queue.append((adj_i, adj_j))
                    visited.add((adj_i, adj_j))

        return -1
            

solution = Solution()
print(solution.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]))