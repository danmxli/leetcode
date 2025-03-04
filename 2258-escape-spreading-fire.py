from typing import List
from collections import deque

# intuition:
# use binary search to find the maximum time the start can wait
# multisource bfs to simulate the fire spreading

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        on_fire = [[False] * n for _ in range(m)]

        # multisource bfs to spread the fire
        def spread_fire(queue: deque):
            new_queue = deque()

            while queue:
                i, j = queue.popleft()
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if grid[ni][nj] == 0 and not on_fire[ni][nj]:
                        on_fire[ni][nj] = True
                        new_queue.append((ni, nj))
            return new_queue
        
        # helper function to check if the start can escape
        def can_escape(time: int) -> bool:

            # reset on_fire
            for i in range(m):
                for j in range(n):
                    on_fire[i][j] = False
            
            fire_queue = deque()
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        on_fire[i][j] = True
                        fire_queue.append((i, j))
            
            while time and fire_queue:
                fire_queue = spread_fire(fire_queue)
                time -= 1
            
            # early return if the fire has reached the start
            if on_fire[0][0]:
                return False

            # bfs to check if the start can escape
            escape_queue = deque([(0, 0)])
            visited = set([(0, 0)])

            while escape_queue:
                for _ in range(len(escape_queue)):
                    i, j = escape_queue.popleft()
                    # if (i, j) == (m - 1, n - 1):
                    #     return True
                    if on_fire[i][j]:
                        continue
                    
                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        ni, nj = i + di, j + dj
                        if not (0 <= ni < m and 0 <= nj < n):
                            continue
                        if grid[ni][nj] == 0 and not on_fire[ni][nj] and (ni, nj) not in visited:
                            if (ni, nj) == (m - 1, n - 1):
                                return True

                            visited.add((ni, nj))
                            escape_queue.append((ni, nj))
                
                fire_queue = spread_fire(fire_queue)

            return False

        # binary search to find the maximum time the start can wait
        left, right = -1, m * n
        while left < right:
            mid = (left + right + 1) // 2
            if can_escape(mid):
                left = mid
            else:
                right = mid - 1
        
        if left == m * n:
            return 1000000000
        return left
sol = Solution()
print(sol.maximumMinutes(grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]))
print(sol.maximumMinutes([[0,0,0,0],[0,1,2,0],[0,2,0,0]]))