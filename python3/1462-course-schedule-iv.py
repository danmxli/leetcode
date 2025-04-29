import math
from typing import List
from collections import defaultdict, deque


class Solution:
    # helper function to print the solution matrix
    def print_solution(self, solution: list[list[int]]):
        for i in range(len(solution)):
            for j in range(len(solution[i])):
                if solution[i][j] == math.inf:
                    print("∞", end=" ")
                else:
                    print(solution[i][j], end=" ")
            print()
    
    # intuition:
    # floyd-warshall algorithm
    # - if there is no path between two courses, then the second course is not a prerequisite for the first course
    def floyd_warshall(self, size: int, graph: list[list[int]]):
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

    def checkIfPrerequisite_dp(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        answer = []
        graph = [[math.inf] * numCourses for _ in range(numCourses)]

        for (source, dest) in prerequisites:
            graph[source][dest] = 1

        dp = self.floyd_warshall(numCourses, graph)
        
        for (source, dest) in queries:
            if dp[source][dest] != math.inf:
                answer.append(True)
            else:
                answer.append(False)

        return answer
    
    def checkIfPrerequisite_bfs_brute(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        isReachable = [[False] * numCourses for _ in range(numCourses)]

        D = defaultdict(list)
        for (source, dest) in prerequisites:
            D[source].append(dest)

        # bfs to find all reachable nodes
        for i in range(numCourses):
            queue = deque([i])
            seen = set()

            while queue:
                node = queue.popleft()
                for neighbor in D[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        isReachable[i][neighbor] = True
                        queue.append(neighbor)

                        # if a node is reachable from the neighbor, then it is reachable from the first node
                        for j in range(numCourses):
                            if isReachable[neighbor][j]:
                                isReachable[i][j] = True

        answer = []
        for (source, dest) in queries:
            answer.append(isReachable[source][dest])
        return answer

# test cases
sol = Solution()
# print(sol.checkIfPrerequisite_bfs_brute(2, [[1,0]], [[0,1],[1,0]]))
# print(sol.checkIfPrerequisite_bfs_brute(2, [], [[1,0],[0,1]]))
# print(sol.checkIfPrerequisite_bfs_brute(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]))
# print(sol.checkIfPrerequisite_bfs_brute(numCourses=5, prerequisites=[[0,1],[1,2],[2,3],[3,4]], queries=[[0,4],[4,0],[1,3],[3,0]]))