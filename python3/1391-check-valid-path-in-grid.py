from typing import List
from collections import defaultdict

# intuition: dfs from node (0,0)

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        M = len(grid)
        N = len(grid[0])

        # data store to help with navigation
        d_next = {
            1: [(0,-1), (0,1)],
            2: [(-1,0), (1,0)],
            3: [(0,-1),(1,0)],
            4: [(0,1),(1,0)],
            5: [(0,-1), (-1,0)],
            6: [(0,1),(-1,0)]
        }
        valid = {
            (1, 0, -1): [1, 4, 6],  # moving left
            (1, 0, 1): [1, 3, 5],   # moving right
            (2, -1, 0): [2, 3, 4],  # moving up
            (2, 1, 0): [2, 5, 6],   # moving down
            (3, 0, -1): [1, 4, 6],  # moving left
            (3, 1, 0): [2, 5, 6],   # moving down
            (4, 0, 1): [1, 3, 5],   # moving right
            (4, 1, 0): [2, 5, 6],   # moving down
            (5, 0, -1): [1, 4, 6],  # moving left
            (5, -1, 0): [2, 3, 4],  # moving up
            (6, 0, 1): [1, 3, 5],   # moving right
            (6, -1, 0): [2, 3, 4]   # moving up
        }

        seen = [[False for _ in range(N)] for _ in range(M)]

        ans = [False]

        def dfs(m, n):
            ...
            if not(0 <= m < M and 0 <= n < N):
                return

            if (m,n) == (M-1,N-1):
                ans[0] = True

            # optimization
            if seen[m][n]:
                return
            
            seen[m][n] = True

            for (d_i, d_j) in d_next[grid[m][n]]:
                adj_m = m+d_i
                adj_n = n+d_j

                if 0 <= adj_m < M and 0 <= adj_n < N:
                    # check validity in both directions
                    curr_cell = (grid[m][n], d_i, d_j)
                    if curr_cell in valid and grid[adj_m][adj_n] in valid[curr_cell]:
                        dfs(adj_m, adj_n)

        dfs(0,0)
        return ans[0]
    
sol = Solution()
print(sol.hasValidPath([[2,4,3],[6,5,2]]))