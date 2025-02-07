"""
https://github.com/gahogg/Data-Structures-and-Algorithms-Theory-Course-Material/blob/main/Python/11%20-%20Graphs%20-%20Edge%20List%2C%20Adjacency%20Matrix%2C%20Adjacency%20List%2C%20DFS%2C%20BFS%20-%20Greg%20Hogg%20DSA%20Course%20Materials%20Lecture%2011.py

graph representation as an adjacency list
an adjacency list is a HASH MAP
 - key is the node id
 - value is a list of all the neighbouring node ids

graph representation as an adjacency matrix
an adjacency matrix is a 2D array
 - rows detail "source" node
 - columns detail "target" node
"""
from collections import defaultdict

A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

D = defaultdict(list)
# populate the hash map
for (u, v) in A:
    D[u].append(v)
    # # undirected graph
    # D[v].append(u)

M = []
n = 8
# init the matrix
for i in range(n):
    M.append([0] * n)
# populate matrix with node-to-node relations
for (u, v) in A:
    M[u][v] = 1
    # # undirected graph
    # M[v][u] = 1

"""
graph traversal algorithms: DFS & BFS
 - time complexity O(V + E)
 - space complexity V + E
 - set that stores the nodes already "seen"

DFS
 - stack
recursive implementation 
iterative implemetation
 
BFS
 - queue
iterative implementation
"""
# optimized python queue implementation using deque
from collections import deque

def dfs_recursive(source: int):
    seen = set()
    seen.add(source)

    def dfs_visit(node: int):
        print(node)
        for adj_node in D[node]:
            if adj_node not in seen:
                seen.add(adj_node)
                dfs_visit(adj_node)

    dfs_visit(source)

def dfs_iterative(source: int):
    seen = set()
    dfs_stack = [source]
    seen.add(source)

    while dfs_stack:
        node = dfs_stack.pop()
        print(node)
        for adj_node in D[node]:
            if adj_node not in seen:
                seen.add(adj_node)
                dfs_stack.append(adj_node)

# # driver
# source = 0
# dfs_recursive(source)

def bfs(source: int):
    bfs_queue = deque()
    seen = set()
    
    # init
    bfs_queue.append(source)
    seen.add(source)

    while bfs_queue:
        node = bfs_queue.popleft()
        print(node)

        # visit adj nodes and mark as seen
        for adj_node in D[node]:
            if adj_node not in seen:
                seen.add(adj_node)
                bfs_queue.append(adj_node)

# # driver
# source = 0
# bfs(source)

"""
topological sort
recursive DFS
does not implement cycle detection
"""

def recursive_dfs_topological_sort(V):
    seen = set()
    ordering_builder = []

    def dfs_visit(node):
        seen.add(node)
        for adj_node in D[node]:
            if adj_node not in seen:
                dfs_visit(adj_node)
        
        ordering_builder.append(node)
        return

    for i in range(V):
        if i not in seen:
            dfs_visit(i)
    
    return ordering_builder[::-1]

# # driver
# A = [[0, 1], [1, 2], [3, 1], [3, 2]]
# D = defaultdict(list)
# for (u,v) in A:
#     D[u].append(v)
# print(recursive_dfs_topological_sort(4))

"""
kahn's algorithm for topological sort using bfs
"""

def bfs_topological_sort(V):

    ordering_builder = []

    # all nodes in the graph
    remaining_nodes = set(range(V))

    # calculate in-degree of each node (aka number of dependencies)
    in_degree = [0] * V
    for node in range(V):
        for adj_node in D[node]:
            in_degree[adj_node] += 1
    
    # add all nodes with in-degree of zero to queue
    bfs_queue = deque()
    for node in range(V):
        if in_degree[node] == 0:
            bfs_queue.append(node)
            remaining_nodes.remove(node)

    while bfs_queue:
        # add nodes without dependencies to ordering
        node = bfs_queue.popleft()
        ordering_builder.append(node)


        # for each adjacent node, decrease the number of dependencies by 1
        for adj_node in D[node]:
            in_degree[adj_node] -= 1
            if in_degree[adj_node] == 0:
                bfs_queue.append(adj_node)
                remaining_nodes.remove(adj_node)

    # if there is a cycle, return empty list
    if remaining_nodes:
        return []
    return ordering_builder

A = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]
D = defaultdict(list)
for (u,v) in A:
    D[u].append(v)
print(bfs_topological_sort(6))


"""
floodfill algorithm, seen in graphs represented as a mxn matrix

"""

