from typing import List
from collections import defaultdict

# intuition
# undirected graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        target_len = len(edges)
        graph = defaultdict(list)
        
        # build the graph
        for (u,v) in edges:
            graph[u].append(v)
            graph[v].append(u)

        for node in graph:
            if len(graph[node]) == target_len:
                return node
            
        return -1