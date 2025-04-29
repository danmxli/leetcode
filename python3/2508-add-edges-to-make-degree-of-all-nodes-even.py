from typing import List
from collections import defaultdict

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        ...
        # undirected graph
        D = defaultdict(set)
        for (u,v) in edges:
            D[u].add(v)
            D[v].add(u)
        
        # find nodes with odd degree
        odd_nodes = []
        for node in D:
            if len(D[node]) % 2 == 1:
                odd_nodes.append(node)
        
        if len(odd_nodes) > 4:
            return False
        
        if len(odd_nodes) % 2 == 1:
            return False

        if len(odd_nodes) == 0:
            return True
        
        # if 2 odd nodes
        if len(odd_nodes) == 2:
            x, y = odd_nodes
            # can connect directly if no edge exists
            if y not in D[x]:
                return True
            # or can connect through any intermediate node
            for i in range(1, n+1):
                if i != x and i != y and i not in D[x] and i not in D[y]:
                    return True
            return False
            
        # if 4 odd nodes
        if len(odd_nodes) == 4:
            a,b,c,d = odd_nodes
            # try all possible pairings
            pairs = [
                [(a,b),(c,d)],
                [(a,c),(b,d)],
                [(a,d),(b,c)]
            ]
            for (x1,y1),(x2,y2) in pairs:
                if y1 not in D[x1] and y2 not in D[x2]:
                    return True
            return False
            
        return True


solution = Solution()
print(solution.isPossible(n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]))
print(solution.isPossible(n = 4, edges = [[1,2],[1,3],[1,4]]))