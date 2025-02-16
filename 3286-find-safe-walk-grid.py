from typing import List
from collections import deque
import math

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        ...
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        weight = [[math.inf] * n for _ in range(m)]

        # init from source i=0, j=0, weight
        queue.append((0,0,grid[0][0]))
        weight[0][0] = grid[0][0]

        while queue:
            curr_i, curr_j, curr_w = queue.popleft()

            # reached dest node
            if (curr_i, curr_j) == (m-1, n-1):
                return True

            for d in [(0,-1), (0,1), (-1,0), (1,0)]:
                adj_i = curr_i + d[0]
                adj_j = curr_j + d[1]


                if not(0 <= adj_i < m) or not(0 <= adj_j < n):
                    continue

                # dijkstra's edge relaxation
                adj_w = grid[adj_i][adj_j]
                new_w = curr_w + adj_w

                # additional health check here (edge case)
                if new_w >= health:
                    continue

                if weight[adj_i][adj_j] > new_w:
                    weight[adj_i][adj_j] = new_w

                    if adj_w == 0:
                        queue.appendleft((adj_i, adj_j, new_w))
                    else:
                        queue.append((adj_i, adj_j, new_w))
        
        return False

solution = Solution()
print(solution.findSafeWalk(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1))
print(solution.findSafeWalk(grid= [[1,1,1,1]], health=4))