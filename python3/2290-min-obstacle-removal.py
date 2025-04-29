from typing import List
from collections import deque
import math
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = deque([(0,0,0,0)]) # curr_weight, obstacles_removed, i, j
        seen = set([(0,0,0)])
        weights = [[math.inf] * n for _ in range(m)]

        weights[0][0] = 0

        while queue:
            curr_weight, obstacles_removed, i, j = queue.popleft()
            if i == m - 1 and j == n - 1:
                return curr_weight

            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                adj_i = i + di
                adj_j = j + dj

                if not (0 <= adj_i < m and 0 <= adj_j < n):
                    continue
                
                if (adj_i, adj_j) in seen:
                    continue
                
                # edge relaxation
                adj_weight = grid[adj_i][adj_j]
                new_weight = curr_weight + adj_weight
                if new_weight < weights[adj_i][adj_j]:
                    
                    weights[adj_i][adj_j] = new_weight

                    # 01 bfs
                    if adj_weight == 0:
                        queue.appendleft((new_weight, obstacles_removed, adj_i, adj_j))
                    else:
                        queue.append((new_weight, obstacles_removed, adj_i, adj_j))

        return weights[m-1][n-1]

sol = Solution()
print(sol.minimumObstacles(grid = [[0,1,1],[1,1,0],[1,1,0]]))
print(sol.minimumObstacles(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))