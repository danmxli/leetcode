from typing import List
import heapq
import math

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])

        weight = [[math.inf] * n for _ in range(m)]
        min_pq = []
        weight[0][0] = 0
        heapq.heappush(min_pq, (0, 0, 0, True)) # True if 1 second, False if 2 seconds
        while min_pq:
            w, i, j, b = heapq.heappop(min_pq)

            if i == m-1 and j == n-1:
                return w

            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni = i + di
                nj = j + dj
                if not(0 <= ni < m and 0 <= nj < n):
                    continue

                new_weight = max(moveTime[ni][nj], weight[i][j]) + (1 if b else 2)
                if weight[ni][nj] > new_weight:
                    weight[ni][nj] = new_weight
                    heapq.heappush(min_pq, (new_weight, ni, nj, not b))
        return -1

sol = Solution()
print(sol.minTimeToReach([[0,4],[4,4]]))
print(sol.minTimeToReach(moveTime = [[0,0,0,0],[0,0,0,0]]))