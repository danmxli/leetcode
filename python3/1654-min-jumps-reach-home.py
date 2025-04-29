from collections import deque
from typing import List

def minimumJumps(forbidden: List[int], a: int, b: int, x: int) -> int:
    # BFS to find the minimum number of jumps to reach x
    # forbidden: list of forbidden positions
    # a: jump length forward
    # b: jump length backward
    # x: target position

    forbidden_set = set(forbidden)
    queue = deque([(0, False)]) # (position, last_backward)
    visited = set([(0, False)])
    moves = -1

    # limiter
    limiter = 6000

    while queue:
        moves += 1
        for _ in range(len(queue)):
            position, last_backward = queue.popleft()
            if position == x:
                return moves
            
            # adjacent position exploration
            # always can go forward
            adj_positions = [(position + a, False)]
            if not last_backward:
                # can only go backward if the last movement was forward
                adj_positions.append((position - b, True))

            for adj_position, is_backward in adj_positions:
                if not(0 <= adj_position < limiter):
                    continue
                if adj_position not in forbidden_set and (adj_position, is_backward) not in visited:

                    visited.add((adj_position, is_backward))
                    queue.append((adj_position, is_backward))

    return -1

print(minimumJumps([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], a = 29, b = 98, x = 80))