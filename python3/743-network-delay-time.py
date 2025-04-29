from collections import defaultdict
from heapq import heappush, heappop, heapify
import math
from typing import List

# min-priority queue implementation
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

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    
    D_weighted = defaultdict(list)

    # build the weighted graph
    for (source, dest, weight) in times:
        D_weighted[source].append((weight, dest))
    
    weights = [math.inf] * (n+1)
    # dijkstra's algorithm
    def dijkstra(source):
        pq = MinPq()

        # init
        weights[source] = 0
        pq.push(0, source)

        while not pq.empty():
            curr_weight, curr_node = pq.pop()
            
            for (weight, dest) in D_weighted[curr_node]:
                # edge relaxation    
                new_weight = curr_weight + weight
                if (weights[dest] > new_weight):
                    weights[dest] = new_weight
                    pq.push(new_weight, dest)
    
    # driver
    dijkstra(k)
    m = max(weights[1:n+1])
    return m if (m < math.inf) else -1


print(networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(networkDelayTime(times = [[1,2,1]], n = 2, k = 2))