from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary as hash table
        table = {}

        for i in range(len(nums)):

            # idea is to store the complement of each number and check if the complement exists in the table
            complement = target - nums[i]            
            if complement in table:
                return [table[complement], i]
            else:
                table[nums[i]] = i            
        return []