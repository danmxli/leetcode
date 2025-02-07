from typing import List
from collections import deque

# intuition:
# 1. use bfs to find the shortest path to the target
# 2. use a set to store the deadends
# 3. use a queue to store the current state
# 4. use a set to store the visited states
# 5. use a variable to store the number of moves

def openLock(deadends: List[str], target: str) -> int:
    dead_set = set(deadends)
    queue = deque(["0000"])
    visited = set(["0000"])
    moves = -1

    if "0000" in dead_set or target in dead_set:
        return moves

    while queue:
        moves += 1
        for _ in range(len(queue)):
            curr = queue.popleft()

            if curr == target:
                return moves
            
            # adjacent states
            for i in range(len(curr)):
                for rotation in [-1, 1]:
                    new_digit = (int(curr[i]) + rotation) % 10
                    adj = curr[:i] + str(new_digit) + curr[i+1:]
                    if adj not in dead_set and adj not in visited:
                        visited.add(adj)
                        queue.append(adj)

    return -1

print(openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))