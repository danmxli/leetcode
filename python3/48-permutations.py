from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index: int, path: List[int]):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] in path:
                    continue

                backtrack(index + 1, path + [nums[i]])

        ans = []
        backtrack(0, [])
        return ans

sol = Solution()
print(sol.permute([1, 2, 3]))