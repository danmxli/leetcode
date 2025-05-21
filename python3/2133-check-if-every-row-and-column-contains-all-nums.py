from typing import List
from collections import defaultdict

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        # row pass
        for i in range(n):
            per_row_values = set([])
            per_col_values = set([])
            for j in range(n):
                if matrix[i][j] not in per_row_values:
                    per_row_values.add(matrix[i][j])
                if matrix[j][i] not in per_col_values:
                    per_col_values.add(matrix[j][i])
            
            if len(per_row_values) != n or len(per_col_values) != n:
                return False
        
        return True
    
sol = Solution()
print(sol.checkValid(matrix = [[1,2,3],[3,1,2],[2,3,1]]))