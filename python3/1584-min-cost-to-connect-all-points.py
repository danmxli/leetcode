from typing import List
from collections import defaultdict
import heapq
import math

# min-priority queue implementation
class MinPq:
    def __init__(self):
        self.heap = []
        
    def push(self, priority, item) -> None:
        heapq.heappush(self.heap, (priority, item))

    def pop(self) -> tuple[int, int]:
        if self.empty():
            raise IndexError("pq is empty")
        
        return heapq.heappop(self.heap)

    def peek(self) -> tuple[int, int]:
        if self.empty():
            raise IndexError("pq is empty")
        
        return self.heap[0]

    def empty(self) -> bool:
        return len(self.heap) == 0

    def size(self) -> int:
        return len(self.heap)
    

def minCostConnectPoints(points: List[List[int]]) -> int:
    # build the adjacency list
    D_weighted = defaultdict(list)
    size = len(points)
    for i in range(size):
        for j in range(i+1, size):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            D_weighted[i].append((dist, j))
            D_weighted[j].append((dist, i))
    
    keys = [math.inf] * size
    in_mst = [False] * size
    pq = MinPq()

    # init
    pq.push(0,0)
    mst_weight = 0

    while not pq.empty():
        # build the MST
        curr_weight, curr_node = pq.pop()
        
        if in_mst[curr_node]:
            continue

        in_mst[curr_node] = True
        mst_weight += curr_weight

        # explore adj nodes
        for (adj_weight, adj_node) in D_weighted[curr_node]:
            ...
            if not in_mst[adj_node] and keys[adj_node] > adj_weight:
                ...
                keys[adj_node] = adj_weight
                pq.push(adj_weight, adj_node)

    return mst_weight

print(minCostConnectPoints(points=[[0,0],[2,2],[3,10],[5,2],[7,0]]))