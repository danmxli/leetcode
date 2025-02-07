from typing import List
from collections import deque

# # STUPID APPROACH
# def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
#     m = len(heights)
#     n = len(heights[0])
#     p_list = set()
#     a_list = set()
    
#     def bfs_visit(i,j) -> int:
#         bfs_queue = deque()
#         seen = set()

#         # init
#         bfs_queue.append((i,j))
#         seen.add((i,j))

#         while bfs_queue:
#             node = bfs_queue.popleft()

#             # explore adj (left right up down)
#             adj_directions = [(-1,0),(1,0),(0,-1),(0,1)]
#             for d in adj_directions:
#                 adj_i = node[0] + d[0]
#                 adj_j = node[1] + d[1]
                
#                 # adjacent to pacific ocean
#                 if adj_i < 0 or adj_j < 0:
#                     p_list.add((i, j))
#                     return
                
#                 # adjacent to atlantic ocean
#                 if adj_i >= m or adj_j >= n:
#                     a_list.add((i, j))
#                     return
                
#                 # continue exploring
#                 if ((adj_i, adj_j) not in seen) and (heights[adj_i][adj_j] <= heights[i][j]):
#                     seen.add((adj_i, adj_j))
#                     bfs_queue.append((adj_i, adj_j))
        
#         # cannot flow to any ocean
#         return
    
#     for i in range(m):
#         for j in range(n):
#             bfs_visit(i,j)

#     return (a_list & p_list)

"""
call bfs twice, per each ocean
seen nodes correspond to nodes that can flow to an ocean
"""

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    
    m = len(heights)
    n = len(heights[0])

    def bfs_visit(nodes: set) -> int:
        # init with the set adjacent to the ocean
        bfs_queue = deque(nodes)
        seen = set(nodes)

        while bfs_queue:
            (i,j) = bfs_queue.popleft()

            # explore adj (left right up down)
            adj_directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for d in adj_directions:
                adj_i = i + d[0]
                adj_j = j + d[1]
                
                # adjacent to pacific ocean or atlantic ocean
                if (adj_i < 0 or adj_j < 0) or (adj_i >= m or adj_j >= n):
                    continue
                
                # continue exploring if the height of the adjacent node is greater
                if ((adj_i, adj_j) not in seen) and (heights[adj_i][adj_j] >= heights[i][j]):
                    seen.add((adj_i, adj_j))
                    bfs_queue.append((adj_i, adj_j))
        
        return seen
    
    # build the coordinates starting at each ocean
    pacific = set((i, 0) for i in range(m)) | set((0, j) for j in range(n))
    atlantic = set((i, n-1) for i in range(m)) | set((m-1, j) for j in range(n))

    p = bfs_visit(pacific)
    a = bfs_visit(atlantic)

    return [[i,j] for (i,j) in (p & a)]

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))