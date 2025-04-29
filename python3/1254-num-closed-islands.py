from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def bfs(i, j):
            queue = deque([(i, j)])
            grid[i][j] = 1
            is_closed = True
            while queue:
                i, j = queue.popleft()
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    is_closed = False
                
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                        queue.append((ni, nj))
                        grid[ni][nj] = 1
            
            return is_closed

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if bfs(i, j):
                        count += 1

        return count

sol = Solution()
print(sol.closedIsland(grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))