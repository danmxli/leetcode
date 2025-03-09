from typing import List
from collections import deque

class Solution:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def seek_first_island(self, grid: List[List[int]]) -> deque:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return

            q.append((i, j))
            grid[i][j] = 0
            for dx, dy in self.directions:
                dfs(i + dx, j + dy)
            
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return q

    def find_shortest_bridge(self, grid: List[List[int]], queue: deque) -> int:
        m = len(grid)
        n = len(grid[0])
        level = 0
        visited = set()
        
        # mark first island as visited
        for i, j in queue:
            visited.add((i, j))
        
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                
                for dx, dy in self.directions:
                    adj_i, adj_j = i + dx, j + dy
                    
                    if 0 <= adj_i < m and 0 <= adj_j < n and (adj_i, adj_j) not in visited:
                        if grid[adj_i][adj_j] == 1:
                            return level
                        
                        visited.add((adj_i, adj_j))
                        queue.append((adj_i, adj_j))
            
            level += 1
        
        return -1

    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = self.seek_first_island(grid)
        return self.find_shortest_bridge(grid, queue)


sol = Solution()
print(sol.shortestBridge([[0,1],[1,0]]))
print(sol.shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]]))