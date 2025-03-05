from typing import List
from collections import deque

# intuition:
# 

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        is_flooded = [[False] * col for _ in range(row)]

        def can_cross(day: int) -> bool:
            # reset is_flooded
            for i in range(row):
                for j in range(col):
                    is_flooded[i][j] = False

            # fill the cells up to day
            for i in range(day):
                x, y = cells[i]
                is_flooded[x - 1][y - 1] = True

            # multisource bfs to check if the start can reach the end
            queue = deque()
            for j in range(col):
                if not is_flooded[0][j]:
                    queue.append((0, j))
            
            if not queue:
                return False
            
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    
                    # reached the bottom
                    if i == row - 1:
                        return True
                    
                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        ni, nj = i + di, j + dj
                        if not (0 <= ni < row and 0 <= nj < col):
                            continue
                        if is_flooded[ni][nj]:
                            continue
                        is_flooded[ni][nj] = True
                        queue.append((ni, nj))
            
            return False


        # binary search
        left, right = 0, len(cells) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if can_cross(mid):
                left = mid
            else:
                right = mid - 1
        
        return left

sol = Solution()
print(sol.latestDayToCross(row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]))
print(sol.latestDayToCross(row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]))
print(sol.latestDayToCross(row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]))