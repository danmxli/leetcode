import math
from typing import List
from collections import defaultdict, deque

# notes:
# - undirected graph
# - bfs
# - patience[i] is the patience of the i-th server
# - return the time when the network becomes idle

def get_finishing_time(distance: int, patience: int) -> int:
    round_trip_time = 2 * distance
    if patience >= round_trip_time:
        last_message_time = 0
    else:
        last_message_time = ((round_trip_time - 1) // patience) * patience

    return last_message_time + round_trip_time

def networkBecomesIdle(edges: List[List[int]], patience: List[int]) -> int:
    
    D = defaultdict(list)
    for (u, v) in edges:
        D[u].append(v)
        D[v].append(u)

    # distances from server 0 to all other servers
    distances = [math.inf] * len(patience)

    # bfs to find distances from server 0 to all other servers
    queue = deque([0])
    seen = set([0])
    time = 0
    distances[0] = 0

    while queue:
        time += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            for adj_node in D[node]:
                if adj_node not in seen:
                    distances[adj_node] = time
                    seen.add(adj_node)
                    queue.append(adj_node)
    
    # find the maximum finishing time
    finishing_time = -1
    for i in range(1, len(distances)):
        finishing_time = max(finishing_time, get_finishing_time(distances[i], patience[i]))

    return finishing_time + 1

print(networkBecomesIdle(edges = [[0,1],[1,2]], patience = [0,2,1]))