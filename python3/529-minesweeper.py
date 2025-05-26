from typing import List

# intuition
# flood-fill continuation when no adjacent mines

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        M = len(board)
        N = len(board[0])
        [row, col] = click
        directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

        # mine condition
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        
        def count_adj_mines(r, c):
            mine_count = 0
            for (d_r, d_c) in directions:
                adj_r, adj_c = r+d_r, c+d_c

                if not(0 <= adj_r < M and 0 <= adj_c < N):
                    continue
                if board[adj_r][adj_c] == "M":
                    mine_count += 1
            return mine_count

        def dfs(r, c):
            # out of bounds
            if not(0 <= r < M and 0 <= c < N):
                return
            
            # skip if not unrevealed
            if board[r][c] != "E":
                return
            
            count = count_adj_mines(r, c)
            if count > 0:
                board[r][c] = str(count)
            else:
                board[r][c] = "B"
                # flood-fill continuation
                for (d_r, d_c) in directions:
                    dfs(r+d_r, c+d_c)

        # unrevealed empty square condition
        dfs(row, col)
        return board

sol = Solution()
print(sol.updateBoard(board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]))