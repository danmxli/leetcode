from itertools import pairwise
import math
from typing import List, Tuple
from collections import deque
import heapq

# intuition:
# dijkstra's algorithm with modified edge relaxation case 😭

class Solution:

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        
        weight = [[math.inf] * n for _ in range(m)]
        min_pq = []
        weight[0][0] = 0
        heapq.heappush(min_pq, (0, 0, 0))
        while min_pq:
            w, i, j = heapq.heappop(min_pq)

            if i == m-1 and j == n-1:
                return w

            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    # moving to adjacent room
                    new_w = max(moveTime[ni][nj], weight[i][j]) + 1
                    if weight[ni][nj] > new_w:
                        weight[ni][nj] = new_w
                        heapq.heappush(min_pq, (new_w, ni, nj))

        return -1

sol = Solution()
print(sol.minTimeToReach([[0,4],[4,4]]))
print(sol.minTimeToReach([[15,58],[67,4]]))
print(sol.minTimeToReach([[17,56],[97,80]]))