from heapq import heappop, heappush
import math
from typing import List
from collections import defaultdict

# minimum cost to make valid path in grid

# min-priority queue implementation
class MinPq:
    def __init__(self):
        self.heap = []
        
    def push(self, priority, item) -> None:
        heappush(self.heap, (priority, item))

    def pop(self) -> tuple[int, any]:
        if self.empty():
            raise IndexError("pq is empty")
        
        return heappop(self.heap)

    def peek(self) -> tuple[int, any]:
        if self.empty():
            raise IndexError("pq is empty")
        
        return self.heap[0]

    def empty(self) -> bool:
        return len(self.heap) == 0

    def size(self) -> int:
        return len(self.heap)

def minCost(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    # directions dictionary
    directions = {
        1: (0,1),
        2: (0,-1),
        3: (1,0),
        4: (-1,0)
    }

    # build directed, weighted graph where grid[i][j] is connected to all the 4 side-adjacent cells
    # weight is 1 if the direction is pointing to the adjacent cell, otherwise 0
    graph = defaultdict(list)
    for i in range(m):
        for j in range(n):
            graph[(i, j)] = []
            for direction, (di, dj) in list(directions.items()):
                ni= i + di
                nj = j + dj
                if (0 <= ni < m) and (0 <= nj < n):
                    weight = 0 if grid[i][j] == direction else 1
                    graph[(i,j)].append((weight, (ni, nj)))

    # dijkstra's to find lowest cost path from (0,0) to (m-1, n-1)
    def dijkstra(source, size_m, size_n) -> int:
        # 2d array to store weights
        weights = [[math.inf] * size_n for _ in range(size_m)]
        weights[source[0]][source[1]] = 0
        pq = MinPq()
        pq.push(0, source)

        while not pq.empty():
            cost, node = pq.pop()
            
            for weight, (ni, nj) in graph[node]:
                new_cost = cost + weight
                if new_cost < weights[ni][nj]:
                    weights[ni][nj] = new_cost
                    pq.push(new_cost, (ni, nj))
        
        return weights[m-1][n-1]
    
    return dijkstra((0,0), m, n)

print(minCost(grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))