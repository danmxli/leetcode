from typing import List
from collections import defaultdict

# OUTPUT LIMIT EXCEEDED FOR BRUTE FORCE SOLUTION
# class Solution:
#     def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
#         # populate the grid
#         grid = [[0 for _ in range(n)] for _ in range(m)]
#         for c in coordinates:
#             grid[c[0]][c[1]] = 1

#         print(grid)
#         # answer data
#         ans = [0 for _ in range(5)]

#         # directions, assume (i,j) is top-left
#         directions = [(1,0),(1,1),(0,1)]

#         for i in range(m):
#             for j in range(n):
#                 is_block = True
#                 count = grid[i][j]

#                 for (d_i, d_j) in directions:
#                     n_i = i + d_i
#                     n_j = j + d_j
#                     if not(0 <= n_i < m and 0 <= n_j < n):
#                         is_block = False
#                         break
#                     count += grid[n_i][n_j]

#                 if is_block:
#                     ans[count] = ans[count] + 1

#         return ans

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        table = defaultdict(int)
        total_blocks = (m-1) * (n-1)

        # answer data
        ans = [0 for _ in range(5)]
        
        # assume block identifier is top-left coordinate
        # for each black cell, identify which 2x2 block it belongs to
        for x,y in coordinates:
            
            # determine top-left of block containing the black coordinate
            for dx in range(-1,1):
                for dy in range(-1,1):
                    n_x = x + dx
                    n_y = y + dy

                    # boundary conditions for block identifier
                    if 0 <= n_x < m-1 and 0 <= n_y < n-1:
                        table[(n_x,n_y)] += 1
                    

        for key in table:
            ans[table[key]] += 1

        ans[0] = total_blocks - sum(ans[1:])
        return ans
    
sol = Solution()
print(sol.countBlackBlocks(m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]]))