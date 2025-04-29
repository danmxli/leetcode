from typing import List
from collections import deque


def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    # floodfill algorithm to iterate over islands of grid2

    m = len(grid1)
    n = len(grid1[0])

    def bfs_visit(i,j) -> int:
        is_subisland = 1
        bfs_queue = deque()
        seen = set()
        
        # init
        grid2[i][j] = 0
        bfs_queue.append((i,j))
        seen.add((i,j))

        if grid1[i][j] == 0:
            is_subisland = 0

        while bfs_queue:
            node = bfs_queue.popleft()
            
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for d in directions:
                adj_i = node[0] + d[0]
                adj_j = node[1] + d[1]

                # seen or grid overflow
                if ((adj_i, adj_j) in seen) or not(0 <= adj_i < m and 0 <= adj_j < n):
                    continue
                
                # grid2 water position
                if grid2[adj_i][adj_j] == 0:
                    continue
                
                # not a subisland if grid1 representation of position is not land
                if grid1[adj_i][adj_j] == 0:
                    is_subisland = 0
                
                # clear out the remaining island
                grid2[adj_i][adj_j] = 0
                seen.add((adj_i, adj_j))
                bfs_queue.append((adj_i, adj_j))
        
        return is_subisland

    # driver
    count = 0
    for i in range(m):
        for j in range(n):
            if grid2[i][j] == 1:
                count += bfs_visit(i,j)

    return count

print(countSubIslands(grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))
print(countSubIslands(grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))