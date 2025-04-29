from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    visited.add((i,j))
                    queue.append((i,j))
        
        distance = -1
        if not queue or len(queue) == n * m:
            return distance
        
        while queue:
            distance += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                    ni, nj = i + di, j + dj
                
                    if (ni, nj) in visited:
                        continue
                    if not (0 <= ni < n and 0 <= nj < m):
                        continue

                    visited.add((ni, nj))
                    queue.append((ni, nj))
        
        return distance


solution = Solution()
print(solution.maxDistance(grid = [[1,0,1],[0,0,0],[1,0,1]]))
print(solution.maxDistance(grid = [[1,0,0],[0,0,0],[0,0,0]]))
