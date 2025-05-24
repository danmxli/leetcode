from typing import List
from collections import defaultdict
import heapq

# intuition
# undirected graph

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for (u,v) in edges:
            # optimization: add to adjacency list if values are > 0
            if vals[v] > 0:
                graph[u].append(v)
            if vals[u] > 0:
                graph[v].append(u)

        # take at most k largest positive weights for each node
        ans = -float('inf')
        for node in range(len(vals)):
            curr_sum = vals[node]
            if node in graph:
                curr_sum += sum(sorted([vals[adj] for adj in graph[node]], reverse=True)[:k])
            ans = max(ans, curr_sum)

        return ans