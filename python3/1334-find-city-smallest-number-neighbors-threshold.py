from typing import List
import math

class Solution:

    # def print_fw(self, answer: list[list[int]]):
    #     for i in range(len(answer)):
    #         for j in range(len(answer[i])):
    #             if answer[i][j] == math.inf:
    #                 print("∞", end=" ")
    #             else:
    #                 print(answer[i][j], end=" ")
    #         print()

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[math.inf] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for u,v,w in edges:
            dp[u][v] = w
            dp[v][u] = w

        for k in range(n): # intermediate node
            for i in range(n): # source node
                for j in range(n): # destination node
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        
        # self.print_fw(dp)

        min_count = math.inf
        min_city = -1
        # iterate through i cities
        for i in range(n):
            count = 0
            for j in range(n):
                if dp[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_count:
                min_count = count
                min_city = i

        return min_city

sol = Solution()
print(sol.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))