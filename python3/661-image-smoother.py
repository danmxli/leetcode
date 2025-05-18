import math
from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        ans = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                sum = 0
                count = 0
                for d_i in range (-1, 2):
                    for d_j in range (-1, 2):
                        adj_i = i + d_i
                        adj_j = j + d_j
                        # out of bounds
                        if 0 > adj_i or adj_i >= m or 0 > adj_j or adj_j >= n:
                            continue

                        sum += img[adj_i][adj_j]
                        count += 1

                print(sum, count)
                ans[i][j] = math.floor(sum / count)
        
        return ans
    
sol = Solution()
# print(sol.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))
print(sol.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))