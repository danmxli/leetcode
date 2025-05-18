from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                n_i = i+1
                n_j = j+1

                if not(0 <= n_i < m and 0 <= n_j < n):
                    continue

                if matrix[i][j] != matrix[n_i][n_j]:
                    return False

        return True
    
