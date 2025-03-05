from typing import List
from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def bfs_visit(i, j) -> int:
            is_enclave = True
            # init
            queue = deque([(i, j)])
            grid[i][j] = 0
            island_size = 1

            while queue:
                x, y = queue.popleft()
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    is_enclave = False

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < m and 0 <= ny < n) or grid[nx][ny] == 0:
                        continue
                    
                    queue.append((nx, ny))
                    grid[nx][ny] = 0
                    island_size += 1
            
            return island_size if is_enclave else 0

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += bfs_visit(i, j)
        return count

        
sol = Solution()
print(sol.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))