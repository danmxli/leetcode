from typing import List

# intuition: binary search on a 2d matrix
# assume a sorted 2d matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = (m*n)-1

        while left <= right:
            mid = (left + right) // 2

            # rows are represented by integer division
            # cols are represented by modulo
            mid_row = int(mid/n)
            mid_col = mid%n
            candidate = matrix[mid_row][mid_col]

            if candidate == target:
                return True
            
            if candidate < target:
                left = mid + 1
            else:
                right = mid - 1

        # exhausted search
        return False