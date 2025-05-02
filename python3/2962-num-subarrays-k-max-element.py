# intuition: shrink window size during "at least" logic
# count number of subarrays where max element appears less than k times

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # total number of possible subarrays from an array of size N
        total = int(N * (N + 1) / 2)

        left = 0
        count = 0
        max_element = max(nums)
        max_element_count = 0
        
        for right in range(N):
            if nums[right] == max_element:
                max_element_count += 1

            # shrink window
            while max_element_count >= k:
                if nums[left] == max_element:
                    max_element_count -= 1
                left += 1

            count += right - left + 1

        return total - count

sol = Solution()
print(sol.countSubarrays(nums = [1,3,2,3,3], k = 2))