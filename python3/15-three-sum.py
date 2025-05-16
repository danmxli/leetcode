from typing import List
from collections import defaultdict

# description:
# given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            # skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # the target is the negative of what the remaining two numbers must sum up to
            target = -nums[i]
            left = i+1
            right = n-1

            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    # skip duplicates for left
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif two_sum > target:
                    right -= 1
                else:
                    left += 1
        
        return ans
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))