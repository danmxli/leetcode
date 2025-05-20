from typing import List
from collections import defaultdict
import heapq

# intuition: numbers with equal row+col are in the same diagonal

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        table = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                table[i+j].append(nums[i][j])

        ans = []
        for key in table:
            for val in reversed(table[key]):
                ans.append(val)

        return ans

sol = Solution()
print(sol.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))