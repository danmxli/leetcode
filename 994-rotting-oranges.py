from typing import List
from collections import deque

"""
intuition
BFS LEVEL TRACKING
"""

def orangesRotting(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    def bfs_visit(nodes: set, target_count: int) -> int:
        # no targets
        if target_count == 0:
            return 0
        
        # init
        time = -1
        bfs_queue = deque(nodes)
        seen = set(nodes)

        while bfs_queue:
            ...
            time += 1
            l = len(bfs_queue)
            for _ in range(l):
                curr = bfs_queue.popleft()

                directions = [(-1,0), (1,0), (0,-1), (0,1)]
                for d in directions:
                    adj_i = curr[0] + d[0]
                    adj_j = curr[1] + d[1]
                    
                    if (not(0 <= adj_i < m)) or (not(0 <= adj_j < n)) or (adj_i, adj_j) in seen:
                        continue

                    if grid[adj_i][adj_j] == 1:
                        seen.add((adj_i, adj_j))
                        bfs_queue.append((adj_i, adj_j))
                        target_count -= 1
        
        if target_count > 0:
            return -1
        return time

    # driver
    rotten = set()
    fresh_count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                rotten.add((i,j))
            if grid[i][j] == 1:
                fresh_count += 1
    
    return bfs_visit(rotten, fresh_count)

print(orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))
# print(orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))