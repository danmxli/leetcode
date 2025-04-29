from typing import Optional
from collections import defaultdict

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# # helper function to build adjacency list
# def build_adj_list(node: Optional['Node']):

#     D = defaultdict(list)

#     def dfs_visit(node: Optional['Node']):
#         if not node:
#             return
#         for neighbor in node.neighbors:
#             D[node.val].append(neighbor.val)
#             dfs_visit(neighbor)

#     dfs_visit(node)
#     return D

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    
    # empty init graph
    if not node:
        return None

    # maintain a hashmap to store visited nodes
    visited = defaultdict()
    
    def dfs_visit(node: Optional['Node']) -> Optional['Node']:
        
        # stop exploration if the node was already visited
        if node.val in visited:
            return visited[node.val]
        
        # create a new copy of the current node and store the object in visited hashmap
        copy = Node(node.val)
        visited[node.val] = copy

        # visit all neighbor nodes
        for nei in node.neighbors:
            nei_copy = dfs_visit(nei)
            copy.neighbors.append(nei_copy)

        # return copy of reference to cloned graph
        return copy
    
    # driver
    return dfs_visit(node)


graph = Node(1, [Node(2, [Node(3)]), Node(4, [Node(5)])])
new_graph = cloneGraph(graph)