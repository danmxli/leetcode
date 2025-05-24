from typing import List
from collections import defaultdict

# intuition
# 1-indexed
# at most one judge
# maintain two stores to track the in-degree and out-degree of each node
# the judge has out-degree of zero and in-degree of n-1

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # directed, unweighted graph
        graph = defaultdict(list)
        out_degree = [0 for _ in range(n)]
        in_degree = [0 for _ in range(n)]

        # build the adjacency list
        for (u,v) in trust:
            graph[u-1].append(v-1)

        # compute in-degree and out-degree
        for node in range(n):
            for adj_node in graph[node]:
                in_degree[adj_node] += 1
                out_degree[node] += 1

        # find the judge
        for node in range(n):
            if out_degree[node] == 0 and in_degree[node] == n-1:
                return node+1
        return -1
    
sol = Solution()
print(sol.findJudge(n = 3, trust = [[1,3],[2,3],[3,1]]))