import math

# return the lease number of perfect squares that sum to n
# intuition: dynamic programming tabulation method
# similar question: coin change

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n+1)]

        # smallest amount is zero, number of squares to sum is zero
        dp[0] = 0

        for root in range(1, int(math.sqrt(n))+1):
            for next in range(root**2, n+1):
                dp[next] = min(dp[next], dp[next - (root**2)]+1)
                
        if dp[n] == float('inf'):
            return -1
        return dp[n]

sol = Solution()
print(sol.numSquares(12))