# 😭 backtracking
from collections import defaultdict
from typing import List

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)
        n = len(values)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = [False] * n
        max_quality = 0

        # https://algo.monster/liteproblems/2065 review solution intuition
        def dfs(current_node: int, remaining_time: int, current_quality: int) -> None:
            nonlocal max_quality

            # If we've reached the start again, consider the value of this path
            if current_node == 0:
                max_quality = max(current_quality, max_quality)
        
            # Recursive exploration of neighbors
            for next_node, travel_time in graph[current_node]:
                if remaining_time - travel_time >= 0:
                    if not visited[next_node]:
                        visited[next_node] = True
                        dfs(next_node, remaining_time - travel_time, current_quality + values[next_node])
                        # Backtrack
                        visited[next_node] = False
                    else:
                        dfs(next_node, remaining_time - travel_time, current_quality)

        # Start from node 0
        visited[0] = True
        dfs(0, maxTime, values[0])
        return max_quality

sol = Solution()
print(sol.maximalPathQuality(values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49))