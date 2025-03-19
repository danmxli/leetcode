from typing import List
from collections import defaultdict

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # color store
        # 0: unvisited
        # 1: red
        # -1: blue
        color = [0] * n

        G = defaultdict(list)
        for i, neighbors in enumerate(graph):
            G[i] = neighbors

        def dfs(node, c) -> bool:
            if color[node] != 0:
                return color[node] == c
            
            color[node] = c
            for neighbor in G[node]:
                if not dfs(neighbor, -c):
                    return False
            return True
        
        for i in range(n):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        return True

sol = Solution()
print(sol.isBipartite(graph = [[1,2,3],[0,2],[0,1,3],[0,2]]))
print(sol.isBipartite(graph = [[1,3],[0,2],[1,3],[0,2]]))