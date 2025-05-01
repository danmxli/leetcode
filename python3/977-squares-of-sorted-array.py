from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        soln = []
        while left <= right:
            l_squared = nums[left] ** 2
            r_squared = nums[right] ** 2

            if l_squared >= r_squared:
                soln.append(l_squared)
                left += 1
            else:
                soln.append(r_squared)
                right -= 1
        
        soln.reverse()
        return soln

sol = Solution()
print(sol.sortedSquares(nums = [-4,-1,0,3,10]))