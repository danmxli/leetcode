from typing import List
from collections import defaultdict, deque

def snakesAndLadders(board: List[List[int]]) -> int:
    N = len(board)
    
    # helper function to map board position to graph position, hella confusing
    def get_position_coordinates(position: int) -> tuple:
        row = (position - 1) // N
        col = (position - 1) % N
        if row % 2 == 1:
            col = N - 1 - col
        return N - 1 - row, col
    
    # bfs
    bfs_queue = deque()
    seen = set()
    # init
    move_count = -1
    bfs_queue.append(1)
    seen.add(1)
    

    while bfs_queue:
        ...
        move_count += 1
        for _ in range(len(bfs_queue)):
            curr = bfs_queue.popleft()
            # win condition
            if curr == N**2:
                return move_count

            # neighbor exploration
            for adj in range(curr+1, min(curr+6, N**2)+1):
                adj_i, adj_j = get_position_coordinates(adj)
                if not(0 <= adj_i < N) or not(0 <= adj_j < N):
                    continue
                
                if board[adj_i][adj_j] != -1:
                    adj = board[adj_i][adj_j]

                if adj not in seen:
                    bfs_queue.append(adj)
                    seen.add(adj)

    return -1

print(snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(snakesAndLadders(board = [[-1,-1],[-1,3]]))