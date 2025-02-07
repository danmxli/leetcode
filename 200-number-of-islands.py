"""
intuition:
when a first "1" is found, use graph traversal to update the adjacent markers to "0" to indicate that island had been visited
visit each marker normally
"""

from typing import List
from collections import deque, defaultdict


def numIslands(grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    count = 0
    
    def dfs_visit(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == "0":
            return
        grid[x][y] = "0"
        dfs_visit(x + 1, y)
        dfs_visit(x - 1, y)
        dfs_visit(x, y + 1)
        dfs_visit(x, y - 1)

    # def bfs_visit(x, y):
    #     grid[x][y] = "0"
    #     bfs_queue = deque()
    #     seen = set()

    #     bfs_queue.append((x,y))
    #     seen.add((x,y))

    #     while bfs_queue:
    #         node = bfs_queue.popleft()

    #         directions = [(-1,0), (1,0), (0,-1), (0,1)]
    #         for d_i, d_j in directions:
    #             new_i = node[0] + d_i
    #             new_j = node[1] + d_j

    #             if (0 <= new_i < m and 0 <= new_j < n):
    #                 # adjacent nodes
    #                 if ((new_i, new_j) not in seen) and (grid[new_i][new_j] == "1"):
    #                     grid[new_i][new_j] = "0"
    #                     seen.add((new_i, new_j))
    #                     bfs_queue.append((new_i, new_j))
    #                 pass

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                dfs_visit(i, j)
                # bfs_visit(i, j)
                count += 1
    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))