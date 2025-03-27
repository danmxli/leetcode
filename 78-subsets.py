from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index: int, path: List[int]):
            ans.append(path[:])

            for i in range(index, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        ans = []
        backtrack(0, [])
        return ans

sol = Solution()

print(sol.subsets([1, 2, 3]))