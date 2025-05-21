from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ...
        # define 3 tables
        row_table = defaultdict(set)
        col_table = defaultdict(set)
        box_table = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in row_table[i]:
                    return False
                else:
                    row_table[i].add(board[i][j])
                
                if board[i][j] in col_table[j]:
                    return False
                else:
                    col_table[j].add(board[i][j])
                
                # box case
                box_i, box_j = int(i//3), int(j//3)
                if board[i][j] in box_table[(box_i,box_j)]:
                    return False
                else:
                    box_table[(box_i,box_j)].add(board[i][j])

        return True
                

sol = Solution()
print(sol.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))