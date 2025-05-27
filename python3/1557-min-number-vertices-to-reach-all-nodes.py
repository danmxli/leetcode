from typing import List
from collections import defaultdict

# intuition
# directed acyclic graph
# count number of nodes with zero incoming edges

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for (u,v) in edges:
            graph[u].append(v)

        # total of n nodes, 0-indexed
        in_degree = [0 for _ in range(n)]
        for node in range(n):
            for adj in graph[node]:
                in_degree[adj] += 1
        
        # return list of nodes with zero incoming edges
        ans = []
        for node in range(n):
            if in_degree[node] == 0:
                ans.append(node)
        return ans