from typing import List
import heapq
from collections import deque

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        queue = deque([start])
        seen = set([tuple(start)])
        level = 0
        heap = []
        
        if pricing[0] <= grid[start[0]][start[1]] <= pricing[1] and grid[start[0]][start[1]] > 1:
            heapq.heappush(heap, (0, grid[start[0]][start[1]], start[0], start[1]))
            
        while queue and len(heap) < k:
            l = len(queue)
            for _ in range(l):
                curr = queue.popleft()
                
                for d in [(0,1), (1,0), (0,-1), (-1,0)]:
                    adj_i = curr[0] + d[0]
                    adj_j = curr[1] + d[1]
                    
                    if not(0 <= adj_i < m and 0 <= adj_j < n) or (adj_i, adj_j) in seen:
                        continue
                        
                    seen.add((adj_i, adj_j))
                    if grid[adj_i][adj_j] == 0:
                        continue
                        
                    if pricing[0] <= grid[adj_i][adj_j] <= pricing[1] and grid[adj_i][adj_j] > 1:
                        heapq.heappush(heap, (level + 1, grid[adj_i][adj_j], adj_i, adj_j))
                    
                    queue.append((adj_i, adj_j))
            level += 1

        result = []
        while heap and len(result) < k:
            _, _, i, j = heapq.heappop(heap)
            result.append([i,j])
            
        return result
         
solution = Solution()
print(solution.highestRankedKItems(grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3))
print(solution.highestRankedKItems([[1,1,1],[0,0,1],[2,3,4]], [2,3], [0,0], 3))
        
        