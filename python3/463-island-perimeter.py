from typing import List
from collections import deque

def islandPerimeter(grid: List[List[int]]) -> int:
    # intuition:
    # bfs to find the island
    # for each node in the island, check its 4 neighbors
    # if the neighbor is water, add 1 to the perimeter
    # if the neighbor is land, add 0 to the perimeter
    # return the perimeter

    m = len(grid)
    n = len(grid[0])

    def bfs_visit(i,j) -> int:
        perimeter = 0
        bfs_queue = deque()
        seen = set()
        
        # init
        bfs_queue.append((i,j))
        seen.add((i,j))

        while bfs_queue:
            node = bfs_queue.popleft()
            
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for d in directions:
                adj_i = node[0] + d[0]
                adj_j = node[1] + d[1]

                if (adj_i, adj_j) in seen:
                    continue
                
                if not((0 <= adj_i < m) and (0 <= adj_j < n)) or (grid[adj_i][adj_j] == 0):
                    perimeter += 1
                else:
                    seen.add((adj_i, adj_j))
                    bfs_queue.append((adj_i, adj_j))
        
        return perimeter
    
    # driver
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return bfs_visit(i,j)
    return 0

print(islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))