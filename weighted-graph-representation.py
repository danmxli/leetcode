from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
import math

"""
shortest single path between two nodes
edge weight can only be 0 or 1
01 bfs yields a time complexity of O(V+E), faster than dijkstra's because it does not use a min-priority queue
"""

A_weighted = [[0,1,0], [0,7,1], [1,7,1], [1,2,1], [2,3,0], [2,5,0], [2,8,1], [3,4,1], [3,5,1], [4,5,1], [5,6,1], [6,7,1], [7,8,1]]
# assume undirected, weighted graph
D_weighted = defaultdict(list)
for (source, dest, weight) in A_weighted:
    D_weighted[source].append((weight, dest))
    D_weighted[dest].append((weight, source))

def weighted_bfs(src: int, v: int):
    ...
    weight = [math.inf] * v
    queue = deque()

    # init from src node
    weight[src] = 0
    queue.append((0, src))

    while queue:
        curr_weight, curr_node = queue.popleft()
        for (adj_weight, adj_node) in D_weighted[curr_node]:
            # dijkstra's edge relaxation
            new_weight = curr_weight + adj_weight
            if weight[adj_node] > new_weight:
                weight[adj_node] = new_weight

                # custom implementation of priority queue using double-ended queue
                # put 0 weight edges to front of queue
                if adj_weight == 0:
                    queue.appendleft((adj_weight, adj_node))
                # put 1 weight edges to back of queue
                else:
                    queue.append((adj_weight, adj_node))

weighted_bfs(src=0, v=9)

"""
dijkstra's algorithm
shortest single path between two nodes
bfs-like implementation, uses a min-priority queue
"""

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
    
    # def build_heap(self, data: list[list[int]]) -> list[tuple[int, int]]:
    #     self.heap = [(weight, dest) for _, dest, weight in data]
    #     heapify(self.heap)

A_weighted = [[2,1,1],[2,3,1],[3,4,1]]
D_weighted = defaultdict(list)

# build the weighted graph
for (source, dest, weight) in A_weighted:
    D_weighted[source].append((weight, dest))

# # dijkstra's algorithm
# # Special example: LC 743. Network Delay Time
# # Note that nodes are labeled 1 to n
# def dijkstra(source, destination, n):
#     predecessors = [-1] * (n+1)
#     weights = [math.inf] * (n+1)
#     pq = MinPq()

#     # init
#     weights[source] = 0
#     pq.push(0, source)

#     while not pq.empty():
#         curr_weight, curr_node = pq.pop()

#         for (weight, dest) in D_weighted[curr_node]:
#             # edge relaxation    
#             new_weight = curr_weight + weight
#             if (weights[dest] > new_weight):
#                 weights[dest] = new_weight
#                 predecessors[dest] = curr_node
#                 pq.push(new_weight, dest)

#     path = []
#     at = destination
#     while at != -1:
#         path.append(at)
#         at = predecessors[at]

#     # TODO check for unreachable
#     if (len(path) == 1 and path[0] == destination and source != destination) or (max(weights[1::n+1]) == math.inf):
#         return ([], -1)
    
#     return (path[::-1], max(weights[1::n+1]))

"""
prim's algorithm to create MST
 - start from min. cost edge
 - returns MST edges and MST weight
"""

A_weighted = [[0,1,4], [0,3,3], [1,2,3], [1,3,5], [1,4,6], [2,4,4], [2,7,2], [3,4,7], [3,5,4], [4,5,5], [4,6,3], [5,6,7], [6,7,5]]
size = 8

D_weighted = defaultdict(list)
for (source, dest, weight) in A_weighted:
    D_weighted[source].append((weight, dest))

def prims(size: int) -> tuple[list, int]:
    predecessors = [-1] * size
    keys = [math.inf] * size
    in_mst = [False] * size
    pq = MinPq()

    # start from the first node
    keys[0] = 0
    pq.push(0, 0)
    mst_edges = []
    mst_weight = 0

    while not pq.empty():
        weight, curr_node = pq.pop()

        # (optional) optimization
        if in_mst[curr_node]:
            continue

        in_mst[curr_node] = True
        mst_weight += weight

        # build the tree using adjacent nodes
        for (weight, dest) in D_weighted[curr_node]:
            if not in_mst[dest] and keys[dest] > weight:
                keys[dest] = weight
                predecessors[dest] = curr_node
                pq.push(weight, dest)

    # MST does not connect all nodes in graph
    if not all(in_mst):
        return([], -1)
    
    for i in range(1, size):
        if predecessors[i] != -1:
            mst_edges.append((predecessors[i], i, keys[i]))
    return (mst_edges, mst_weight)

# source = 0
# prims(size)

"""
kruskal's algorithm to create MST
new ADT: disjoint set
new algo: union find
"""

"""
initially all elements belong to diff sets
select a set member to be the representative (i.e. the parent)
 - base case:
    - the representative element is when the parent of the element == element
perform union of two sets i,j: repr. of set i becomes repr. of set j
maintain a set of parents of each element
"""
class DisjointSet:
    def __init__(self, size: int):
        # init parent with each element as its own representative
        self.parent = list((range(size)))
        # init rank of each to 0
        # rank is used to optimize the union operation
        self.rank = [0] * size

    def find_representative(self, i):
        # similar to traversing from head to last node of a linked list
        if self.parent[i] == i:
            return i
        return self.find_representative(self.parent[i])

    def unite(self, i, j):
        i_r = self.find_representative(i)
        j_r = self.find_representative(j)
        
        # make the representative of set i be the representative of set j if the rank of i is less than j, and vice versa
        if self.rank[i_r] < self.rank[j_r]:
            self.parent[i_r] = j_r
        elif self.rank[i_r] > self.rank[j_r]:
            self.parent[j_r] = i_r
        else:
            self.parent[j_r] = i_r
            self.rank[i_r] += 1
        
    def in_same_set(self, a, b):
        # determine if elements a,b are in the same set
        return self.find_representative(a) == self.find_representative(b)


def kruskal(edges: list[tuple[int, int, int]], size: int):
    
    mst = []

    # sort edges by smallest first
    sorted_edges = sorted(edges, key=lambda x: x[2])

    # init disjoint set
    d_set = DisjointSet(size)

    # iterate through sorted edges
    for (source, dest, weight) in sorted_edges:
        # add edge to mst if they are not in the same set
        if not d_set.in_same_set(source, dest):
            d_set.unite(source, dest)
            mst.append((source, dest, weight))

    return mst

# driver
# A_weighted = [
#     (7, 6, 1),
#     (8, 2, 2),
#     (6, 5, 2),
#     (0, 1, 4),
#     (2, 5, 4),
#     (8, 6, 6),
#     (2, 3, 7),
#     (7, 8, 7),
#     (0, 7, 8),
#     (1, 2, 8),
#     (3, 4, 9),
#     (5, 4, 10),
#     (1, 7, 11),
#     (3, 5, 14)
# ]
# size = 9
A_weighted = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
size = 4

# D_weighted = defaultdict(list)

# for (source, dest, weight) in A_weighted:
#     D_weighted[source].append((weight,dest))

"""
floyd-warshall algorithm (all pairs shortest path)

overview:
 - init solution matrix with inf
 - iterate through each node as an intermediate node
 - for each pair of nodes, check if the path through the intermediate node is shorter than the current shortest path
 - update the shortest path if it is

time complexity: O(n^3)
space complexity: O(n^2)
"""

def floyd_warshall(size: int, graph: list[list[int]]):
    # init solution matrix with inf
    solution = [[math.inf] * size for _ in range(size)]

    # init solution matrix with graph
    for i in range(size):
        for j in range(size):
            solution[i][j] = graph[i][j]

    for k in range(size): # intermediate node
        for i in range(size): # source node
            for j in range(size): # destination node
                solution[i][j] = min(solution[i][j], solution[i][k] + solution[k][j])

    return solution

def print_solution(solution: list[list[int]]):
    for i in range(len(solution)):
        for j in range(len(solution[i])):
            if solution[i][j] == math.inf:
                print("∞", end=" ")
            else:
                print(solution[i][j], end=" ")
        print()

# graph construction
graph = [[0, 5, math.inf, 10],
         [math.inf, 0, 3, math.inf],
         [math.inf, math.inf, 0,   1],
         [math.inf, math.inf, math.inf, 0]
         ]
print_solution(floyd_warshall(4, graph))