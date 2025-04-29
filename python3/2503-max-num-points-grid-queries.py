from typing import List
from collections import deque
import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        l = len(queries)

        # answer array
        answer = [0] * l

        # sort the queries knowing their original order
        queries = sorted(enumerate(queries), key=lambda x: x[1])
        print(queries)
        
        # maintain a min pq of the points
        pq = [(grid[0][0], 0, 0)]
        seen = set([(0,0)])
        prev_count = 0

        for pointer in range(l):
            count = prev_count
            while pq:

                # check if finished with the current query
                val, i, j = pq[0]
                if val >= queries[pointer][1]:
                    break
                
                heapq.heappop(pq)
                count += 1

                for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                    adj_i = i + di
                    adj_j = j + dj

                    if not (0 <= adj_i < m and 0 <= adj_j < n):
                        continue
                    
                    if (adj_i, adj_j) in seen:
                        continue
                    
                    seen.add((adj_i, adj_j))
                    heapq.heappush(pq, (grid[adj_i][adj_j], adj_i, adj_j))

            answer[queries[pointer][0]] = count
            prev_count = count
        return answer

sol = Solution()
print(sol.maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]))
        
