from collections import deque
from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    max_area = 0

    def bfs_visit(x, y) -> int:
        bfs_queue = deque()
        seen = set()

        # init
        bfs_queue.append((x,y))
        seen.add((x,y))
        grid[x][y] = 0
        count = 1

        while bfs_queue:
            node = bfs_queue.popleft()

            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for d_i, d_j in directions:
                new_i = node[0] + d_i
                new_j = node[1] + d_j

                if (0 <= new_i < m and 0 <= new_j < n):
                    # adjacent nodes
                    if ((new_i, new_j) not in seen) and (grid[new_i][new_j] == 1):
                        seen.add((new_i, new_j))
                        grid[new_i][new_j] = 0
                        bfs_queue.append((new_i, new_j))
                        count += 1

        return count

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                max_area = max(max_area, bfs_visit(i,j))

    return max_area

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))