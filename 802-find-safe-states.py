from collections import deque, defaultdict

# bfs (khan's algorithm) intuition:
# reverse the graph
def eventualSafeNodes_bfs(graph: list[list[int]]) -> list[int]:
    n = len(graph)
    # build the adjacency list of the reverse graph
    D = defaultdict(list, {node: [] for node in range(n)})
    for node in range(n):
        for adj_node in graph[node]:
            D[adj_node].append(node)

    in_degree = [0] * n
    for node in range(n):
        for adj_node in D[node]:
            in_degree[adj_node] += 1

    queue = deque()
    for node in range(n):
        if in_degree[node] == 0:
            queue.append(node)

    ordering = []
    while queue:
        node = queue.popleft()
        ordering.append(node)
        
        for adj_node in D[node]:
            in_degree[adj_node] -= 1
            if in_degree[adj_node] == 0:
                queue.append(adj_node)    

    return sorted(ordering)

# dfs intuition:
# bro 😭
# find all nodes without cycles
def eventualSafeNodes_dfs(graph: list[list[int]]) -> list[int]:

    cycle = set()
    seen = set()

    def dfs(node):
        if node in cycle:
            return False
        if node in seen:
            return True
        
        cycle.add(node)
        for adj_node in graph[node]:
            if not dfs(adj_node):
                return False
        cycle.remove(node)
        seen.add(node)
        return True
    
    n = len(graph)
    safe = []
    for node in range(n):
        if dfs(node):
            safe.append(node)
        seen.add(node)
    return safe

# print(eventualSafeNodes_bfs([[1,2],[2,3],[5],[0],[5],[],[]]))
print(eventualSafeNodes_dfs([[1,2],[2,3],[5],[0],[5],[],[]]))