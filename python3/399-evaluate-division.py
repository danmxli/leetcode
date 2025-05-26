from typing import List
from collections import deque, defaultdict
import heapq

# intuition
# bfs
# weighted, directed graph
# nodes are division operands
# edges are results per division

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        N = len(equations)
        # build the adjacency list
        graph = defaultdict(list)
        for i in range(N):
            u = equations[i][0]
            v = equations[i][1]
            w = values[i]
            graph[u].append((w,v))
            graph[v].append((1/w,u))

        def find_path(source, dest):
            # check if nodes exist in graph
            if source not in graph or dest not in graph:
                return -1
            
            # divide by itself
            if source == dest:
                return 1.0

            visited = set()
            # accumulate the answer
            q = deque([(1.0, source)])
            visited.add(source)

            while q:
                curr_weight, curr_node = q.popleft()
                if curr_node == dest:
                    return curr_weight
                
                for (adj_weight, adj_node) in graph[curr_node]:
                    if adj_node not in visited:
                        new_weight = curr_weight * adj_weight
                        visited.add(adj_node)
                        q.append((new_weight, adj_node))
        
            return -1.0
        
        # total query solution
        soln = []
        for (s, d) in queries:
            soln.append(find_path(s, d))
        return soln


sol = Solution()
print(sol.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))