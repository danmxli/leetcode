from math import comb
from typing import List

# intuition:
# 1. use dfs to find the number of ways to reorder the array
# 2. use memoization to store the number of ways to reorder the array
# 3. use a visited set to avoid revisiting the same array
# 4. use a direction array to traverse the array

def numOfWays(nums: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)

    def count_bst(nums: List[int]) -> int:
        if len(nums) <= 1:
            return 1
 
        left = [num for num in nums if num < nums[0]]
        right = [num for num in nums if num > nums[0]]
        left_ways = count_bst(left)
        right_ways = count_bst(right)
        left_size = len(left)
        right_size = len(right)
        return ((comb[left_size + right_size][left_size] * left_ways) % MOD) * right_ways % MOD

    comb = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        comb[i][0] = 1

    for i in range(1, n):
        for j in range(1, i + 1):
            comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % MOD

    return (count_bst(nums) - 1 + MOD) % MOD

if __name__ == "__main__":
    nums = [2,1,3]
    print(numOfWays(nums))