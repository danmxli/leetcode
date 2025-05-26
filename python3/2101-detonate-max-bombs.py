from typing import List
from collections import defaultdict

# intuition
# directed, unweighted graph
# one none is connected to another if the larger blast radius of the two contains the other
# run dfs from all nodes

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        N = len(bombs)
        for i in range(N):
            (x1, y1, r1) = bombs[i]

            for j in range(N):
                if i == j:
                    continue
                
                (x2, y2, _) = bombs[j]
                # squared distance between bombs i and j
                distance_squared = ((x2-x1) ** 2) + ((y2-y1) ** 2)
                radius_squared = r1 ** 2

                if radius_squared >= distance_squared:
                    graph[i].append(j)

        def dfs(node):
            visited[node] = True
            count[0] += 1
            for adj in graph[node]:
                if not visited[adj]:
                    dfs(adj)

        # from all nodes
        ans = 0
        for node in range(N):
            count = [0]
            visited = [False for _ in range(N)]
            dfs(node)
            ans = max(ans, count[0])

        return ans

sol = Solution()
print(sol.maximumDetonation(bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))