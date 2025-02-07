# lc 2203. Minimum Weighted Subgraph Required Paths
# intuition:
# 1. find the shortest path from node 1 to node n
# 2. find the shortest path from node n to node 1
# 3. return the sum of the two paths

# THIS IS WRONG, SEE THE SOLUTION FOR THE CORRECT ANSWER 😭

from heapq import heappop, heappush
import math
from typing import List
from collections import defaultdict

class MinPq:
    def __init__(self):
        self.heap = []

    def push(self, priority, item) -> None:
        heappush(self.heap, (priority, item))

    def pop(self) -> tuple[int, int]:
        if self.empty():
            raise IndexError("pq is empty")
        
        return heappop(self.heap)

    def peek(self) -> tuple[int, int]:
        if self.empty():
            raise IndexError("pq is empty")
        
        return self.heap[0]

    def empty(self) -> bool:
        return len(self.heap) == 0

    def size(self) -> int:
        return len(self.heap)

def minimumWeight(n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
    ...
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)

    for (source, dest, weight) in edges:
        graph[source].append((weight, dest))
        reverse_graph[dest].append((weight, source))

    print(reverse_graph)

    # dijkstra's algorithm
    def dijkstra(source, graph) -> list[any]:
        weights = [math.inf] * (n)
        pq = MinPq()
        weights[source] = 0
        pq.push(0, source)

        while not pq.empty():
            curr_weight, curr_node = pq.pop()

            # optimization
            if curr_weight != weights[curr_node]:
                continue

            for (adj_weight, adj_node) in graph[curr_node]:
                # edge relaxation
                new_weight = curr_weight + adj_weight
                if new_weight < weights[adj_node]:
                    weights[adj_node] = new_weight
                    pq.push(new_weight, adj_node)
        
        return weights

    # get distances from src1 to all nodes
    dist_from_src1 = dijkstra(src1, graph)
    # get distances from src2 to all nodes
    dist_from_src2 = dijkstra(src2, graph)
    # get distances from dest to all nodes
    dist_from_dest = dijkstra(dest, reverse_graph)

    # find the minimum weight path from src1 to src2 to dest
    ans = min(sum(v) for v in zip(dist_from_src1, dist_from_src2, dist_from_dest))
    return -1 if ans >= math.inf else ans

# print(minimumWeight(n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5))
print(minimumWeight(n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2))