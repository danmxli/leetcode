from typing import List
import heapq
import math

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        min_pq = []
        weights = [[math.inf] * n for _ in range(m)]
        weights[0][0] = grid[0][0]
        heapq.heappush(min_pq, (grid[0][0],0,0)) # weight,i,j
        
        while min_pq:
            w,i,j = heapq.heappop(min_pq)
            if (i,j) == (m-1,n-1):
                return w
            
            for d in [(0,-1),(0,1),(-1,0),(1,0)]:
                adj_i = i + d[0]
                adj_j = j + d[1]

                if not(0 <= adj_i < m) or not(0 <= adj_j < n):
                    continue

                # edge relaxation
                new_w = max(weights[i][j], grid[adj_i][adj_j])
                if weights[adj_i][adj_j] > new_w:
                    weights[adj_i][adj_j] = new_w
                    heapq.heappush(min_pq, (new_w,adj_i,adj_j))
        
        return -1

sol = Solution()
print(sol.swimInWater(grid=[[3,2],[0,1]]))
# print(sol.swimInWater(grid = [[0,2],[1,3]]))
# print(sol.swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))