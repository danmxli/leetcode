from typing import List
from collections import deque
import heapq
import math

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # early return if impossible
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        # time to reach cell i, j
        weight = [[math.inf] * n for _ in range(m)]
        weight[0][0] = 0

        # pq caries {time, cell_i, cell_j}
        pq = [(0, 0, 0)]

        # optimization
        seen = set({(0, 0)})

        while pq:
            time, i, j = heapq.heappop(pq)
            if i == m - 1 and j == n - 1:
                return time
            
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                adj_i = i + di
                adj_j = j + dj

                if not (0 <= adj_i < m and 0 <= adj_j < n):
                    continue

                if (adj_i, adj_j) in seen:
                    continue

                time_diff = grid[adj_i][adj_j] - time
                if time >= grid[adj_i][adj_j]:
                    wait = 1
                elif time_diff % 2 == 1:
                    wait = 0
                # cannot stay still
                else:
                    wait = 1

                # modified edge relaxation
                # new_time = wait + grid[adj_i][adj_j]
                # if new_time < weight[adj_i][adj_j]:
                #     weight[adj_i][adj_j] = new_time
                #     heapq.heappush(pq, (new_time, adj_i, adj_j))
                new_time = max(time + 1, grid[adj_i][adj_j] + wait)
                heapq.heappush(pq, (new_time, adj_i, adj_j))
                seen.add((adj_i, adj_j))

        return -1

solution = Solution()
print(solution.minimumTime(grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]))
# print(solution.minimumTime(grid = [[0,2,4],[3,2,1],[1,0,4]]))