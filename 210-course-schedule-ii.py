from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        ordering_builder = []

        # dictionary
        D = defaultdict(list)
        for (u,v) in prerequisites:
            D[u].append(v)

        # all nodes in the graph
        remaining_nodes = set(range(numCourses))

        # calculate in-degree of each node (aka number of dependencies)
        in_degree = [0] * numCourses
        for node in range(numCourses):
            for adj_node in D[node]:
                in_degree[adj_node] += 1

        # add all nodes with in-degree of zero to queue
        bfs_queue = deque()
        for node in range(numCourses):
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

        # cycle detection
        if remaining_nodes:
            return []
        return ordering_builder[::-1]
        
    numCourses = 2
    prerequisites = [[0, 1]]