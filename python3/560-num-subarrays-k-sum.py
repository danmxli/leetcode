# intuition: prefix sum and hash table
# store the frequency of the running sum while traversing the array
# if there is an running sum - k in the table, it means there exists a subarray whose sum is equal to k
# note: use DefaultDict

from typing import List, DefaultDict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = DefaultDict(int)
        sum = 0
        count = 0

        for i in range (0, len(nums)):
            sum += nums[i]
            
            if sum == k:
                count += 1
            if (sum-k) in store:
                count += store[sum-k]
            
            store[sum] += 1

        return count

sol = Solution()
print(sol.subarraySum(nums = [1,1,1], k = 2))