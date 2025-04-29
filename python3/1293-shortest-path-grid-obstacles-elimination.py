from typing import List
from collections import deque

# intuition:
# bfs with level tracking
# maintain a tuple of (i, j, k), where k is the number of obstacles we have eliminated

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        # manhattan distance optimization
        if k >= n + m - 2:
            return n + m - 2

        visited = set()
        queue = deque()
        # init with i, j, k
        queue.append((0,0,k))
        visited.add((0,0,k))
        distance = -1
        while queue:
            distance += 1
            for _ in range(len(queue)):
                i, j, remaining_k = queue.popleft()
                if i == n-1 and j == m-1:
                    return distance
                for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                    ni, nj = i + di, j + dj

                    # if not (0 <= ni < n and 0 <= nj < m):
                    #     continue
                    # if (ni, nj, k) in visited:
                    #     continue

                    # if grid[ni][nj] == 1:
                    #     # destroyed all k obstacles
                    #     if k == k_max:
                    #         continue
                    #     else:
                    #         # add to queue and visited, increment k
                    #         queue.append((ni, nj, k+1))
                    #         visited.add((ni, nj, k+1))
                    # else:
                    #     # add to queue and visited, no increment
                    #     queue.append((ni, nj, k))
                    #     visited.add((ni, nj, k))
                    if (0 <= ni < n and 0 <= nj < m):
                        new_k = remaining_k - grid[ni][nj]
                        state = (ni, nj, new_k)
                        if state not in visited and new_k >= 0:
                            visited.add(state)
                            queue.append(state)

        # exhausted all cells
        return -1

solution = Solution()
print(solution.shortestPath(grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1))
print(solution.shortestPath(grid = [[0,0,1,0,0,0,0,1,0,1,1,0,0,1,1],[0,0,0,1,1,0,0,1,1,0,1,0,0,0,1],[1,1,0,0,0,0,0,1,0,1,0,0,1,0,0],[1,0,1,1,1,1,0,0,1,1,0,1,0,0,1],[1,0,0,0,1,1,0,1,1,0,0,1,1,1,1],[0,0,0,1,1,1,0,1,1,0,0,1,1,1,1],[0,0,0,1,0,1,0,0,0,0,1,1,0,1,1],[1,0,0,1,1,1,1,1,1,0,0,0,1,1,0],[0,0,1,0,0,1,1,1,1,1,0,1,0,0,0],[0,0,0,1,1,0,0,1,1,1,1,1,1,0,0],[0,0,0,0,1,1,1,0,0,1,1,1,0,1,0]], k = 27))
