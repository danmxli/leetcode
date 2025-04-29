from typing import List

"""
GG
"""

def rob(nums: List[int]) -> int:
    memo = {}
    
    def rob_helper(nums: List[int], i: int) -> int:
        
        # avoid recompute
        if i in memo:
            return memo[i]

        # recursive implementation
        if i >= len(nums):
            return 0
        memo[i] = max(nums[i] + rob_helper(nums, i+2), rob_helper(nums, i+1))
        return memo[i]
    
    return rob_helper(nums, 0)

print(rob(nums = [2,7,9,3,1]))