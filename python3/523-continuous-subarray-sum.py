# intuition, requires math background
# track the running remainder, and the earliest index of each

from typing import List, DefaultDict

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        store = DefaultDict(int)
        # edge case where valid subarray starts at index zero
        store[0] = -1
        running_sum = 0

        for i in range (0, len(nums)):
            running_sum += nums[i]
            running_rem = running_sum % k

            if running_rem not in store:
                store[running_rem] = i
            elif abs(store[running_rem] - i) >= 2:
                return True

        return False
    
sol = Solution()
print(sol.checkSubarraySum(nums = [23,2,4,6,7], k = 6))
print(sol.checkSubarraySum(nums = [23,2,6,4,7], k = 13))