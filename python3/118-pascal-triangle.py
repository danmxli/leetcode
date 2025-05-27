from typing import List

# intuition
# row[i][j] = row[i-1][j-1] + row[i-1][j] internal values
# edges have the value of 1
# 2d-dp tabulation

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # build the triangle
        dp = [[0] * (i+1) for i in range(numRows)]

        # populate the triangle
        for i in range(numRows):
            for j in range(i+1):
                # base case
                if j == 0 or i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp

sol = Solution()
print(sol.generate(5))