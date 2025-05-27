from typing import List
from collections import defaultdict, deque

# intuition
# directed, weighted graph rooted at zero
# bfs from zero, multiply weights on path

class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        N = len(conversions)+1
        baseUnitConversion = [0 for _ in range(N)]

        graph = defaultdict(list)
        for (u,v,w) in conversions:
            graph[u].append((w,v))

        # init: at unit type zero, conversion to self done take multiplication by 1
        q = deque([(1, 0)])

        while q:
            (curr_w, curr_node) = q.popleft()
            baseUnitConversion[curr_node] = curr_w

            for (adj_w, adj_node) in graph[curr_node]:
                new_w = (curr_w * adj_w) % (10**9 + 7)
                q.append((new_w, adj_node))

        return baseUnitConversion