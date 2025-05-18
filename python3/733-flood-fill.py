from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        # init
        to_replace = image[sr][sc]
        image[sr][sc] = color
        q = deque()
        q.append((sr, sc))

        while q:
            (curr_i, curr_j) = q.popleft()

            for (d_i, d_j) in directions:
                adj_i = curr_i + d_i
                adj_j = curr_j + d_j

                # out of bounds
                if 0 > adj_i or adj_i >= m or 0 > adj_j or adj_j >= n:
                    continue

                # optimization
                if image[adj_i][adj_j] == color:
                    continue

                # flood the adj coord
                if image[adj_i][adj_j] == to_replace:
                    image[adj_i][adj_j] = color
                    q.append((adj_i, adj_j))

        return image
    
sol = Solution()
print(sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))