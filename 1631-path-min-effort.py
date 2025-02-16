from typing import List
from collections import deque, defaultdict
import heapq
import math

# intuition:
# SIMILAR TO LC 3341

class Solution:

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        min_pq = []
        weights = [[math.inf] * n for _ in range(m)]
        weights[0][0] = 0
        heapq.heappush(min_pq, (0,0,0)) # weight,i,j
        
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
                new_w = max(weights[i][j], abs(heights[i][j] - heights[adj_i][adj_j]))
                if weights[adj_i][adj_j] > new_w:
                    weights[adj_i][adj_j] = new_w
                    heapq.heappush(min_pq, (new_w,adj_i,adj_j))
        
        return -1


sol = Solution()
print(sol.minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]]))
# print(sol.minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))