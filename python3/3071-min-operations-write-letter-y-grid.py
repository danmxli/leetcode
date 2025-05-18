from typing import List

# intuition: counting
# start from the center cell, n // 2
# maintain a list of positions for each:
# left segment 
# right segment
# bottom segment

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        N = len(grid)
        cx = N // 2
        left_seg = set([(x,x) for x in range(0, cx)])
        right_seg = set([(N-1-x, x) for x in range(N-1, cx, -1)])
        bottom_seg = set([(x, cx) for x in range(cx, N)])

        # pythonic set operations
        y_set = left_seg.union(right_seg).union(bottom_seg)
        grid_set = set((x,y) for x in range(N) for y in range(N))
        remaining = grid_set - y_set

        min_ops = float('inf')

        # count the number of operations to complete the y, and number of operations to flood the remaining coordinates
        def count_ops(y_val, rem_val) -> int:
            diff_y_val = 0
            diff_rem_val = 0

            for i in range(N):
                for j in range(N):
                    if (i,j) in y_set and grid[i][j] != y_val:
                        diff_y_val += 1
                    
                    if (i,j) in remaining and grid[i][j] != rem_val:
                        diff_rem_val += 1
            
            return diff_y_val + diff_rem_val
        
        # iterate through the number of operations 0,1,2
        for y_val in range(0,3):
            for rem_val in range(0,3):
                if y_val != rem_val:
                    min_ops = min(min_ops, count_ops(y_val, rem_val))

        return min_ops
sol = Solution()
print(sol.minimumOperationsToWriteY([[1,2,2],[1,1,0],[0,1,0]]))