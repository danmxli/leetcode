from typing import List
from collections import defaultdict, deque

# intuition
# directed, unweighted graph

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        graph = defaultdict(list)
        
        for u in range(n):
            if edges[u] != -1:
                graph[u].append(edges[u])

        # bfs helper to find distances from source to all nodes
        def bfs(source) -> List[int]:
            q = deque([source])
            seen = set([source])
            distances = [float('inf') for _ in range(n)]
            dist = -1

            while q:
                l = len(q)
                dist += 1

                for _ in range(l):
                    curr = q.popleft()
                    distances[curr] = dist
                    
                    for adj in graph[curr]:
                        if adj in seen:
                            continue

                        seen.add(adj)
                        q.append(adj)

            return distances
        
        reachable_from_1 = bfs(node1)
        reachable_from_2 = bfs(node2)

        ans = -1
        min = float('inf')

        for curr in range(n):

            if reachable_from_1[curr] != -1 and reachable_from_2[curr] != -1:
                candidate = max(reachable_from_1[curr], reachable_from_2[curr])
                if candidate < min:
                    min = candidate
                    ans = curr

        return ans
        
sol = Solution()
print(sol.closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))