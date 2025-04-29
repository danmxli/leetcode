from typing import List

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        m = len(board)
        n = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for dr, dc in directions:
            r = rMove + dr
            c = cMove + dc
            count = 1
            
            # neighbor exploration
            while 0 <= r < m and 0 <= c < n:
                # encountered an empty cell
                if board[r][c] == ".":
                    break

                # encountered a cell with the same color
                if board[r][c] == color:
                    if count >= 2:
                        return True
                    break

                r += dr
                c += dc
                count += 1

        return False
sol = Solution()