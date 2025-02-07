from collections import deque
from typing import List
import copy

"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
"""

def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # intuition:
    # init dummy board to track visited cells
    # bfs on each region returns list of cells to be replaced, or empty list if the region is not surrounded

    dummy_board = copy.deepcopy(board)
    m = len(board)
    n = len(board[0])

    def bfs_visit(i,j):
        is_surrounded = True
        bfs_queue = deque()
        seen = set()
        
        # init
        dummy_board[i][j] = "X"
        bfs_queue.append((i,j))
        seen.add((i,j))

        while bfs_queue:
            node = bfs_queue.popleft()
            
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for d in directions:
                adj_i = node[0] + d[0]
                adj_j = node[1] + d[1]

                if (adj_i, adj_j) in seen:
                    continue
                
                # region is on edge of board
                if not(0 <= adj_i < m and 0 <= adj_j < n):
                    is_surrounded = False
                    continue
                
                if board[adj_i][adj_j] == "X":
                    continue
                
                # clear out the dummy
                dummy_board[adj_i][adj_j] = "X"
                seen.add((adj_i, adj_j))
                bfs_queue.append((adj_i, adj_j))

        return seen if is_surrounded else set()
    
    # driver
    for i in range(m):
        for j in range(n):
            if dummy_board[i][j] == "O":
                cells_to_replace = bfs_visit(i,j)
                if not cells_to_replace:
                    continue
                
                for cell in cells_to_replace:
                    board[cell[0]][cell[1]] = "X"

    return

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(board)
print(board)