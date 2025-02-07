from typing import List
import math

"""
GG
"""

def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    dp = [0] * (n+1)
    dp[n-1] = cost[n-1]
    dp[n-2] = cost[n-2]

    for i in range((n-3), -1, -1):
        dp[i] = cost[i] + min(dp[i+1], dp[i+2])
    
    return min(dp[0], dp[1])

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))