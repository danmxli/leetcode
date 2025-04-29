from typing import List
from collections import defaultdict
import heapq
import math

# intuition:
# dijkstra's algorithm with modified edge relaxation case
# i need to study graph theory more
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        # weighted undirected graph
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        n = len(graph)
        cost = [math.inf] * n
        time = [maxTime+1] * n
        min_pq = []
        # prioritizes minimum cost
        heapq.heappush(min_pq, (passingFees[0], 0, 0))
        cost[0] = passingFees[0]
        time[0] = 0
        
        while min_pq:
            c, t, node = heapq.heappop(min_pq)
            if node == n-1:
                return cost[n-1]
            # optimization
            if c > cost[node] and t > time[node]:
                continue

            for nei_n, nei_t in graph[node]:
                new_time = t + nei_t
                # optimization
                if new_time > maxTime:
                    continue
                new_cost = c + passingFees[nei_n]
                # first, ensure that the cost is the minimum
                if new_cost < cost[nei_n]:
                    cost[nei_n] = new_cost
                    time[nei_n] = new_time
                    heapq.heappush(min_pq, (new_cost, new_time, nei_n))
                # second, ensure that the time is the minimum
                elif new_time < time[nei_n]:
                    time[nei_n] = new_time
                    heapq.heappush(min_pq, (new_cost, new_time, nei_n))
        return -1