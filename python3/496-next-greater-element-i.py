from typing import List
from collections import defaultdict

# non brute force intuition
# hash table stores data from nums1, mapping value -> index in list

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = defaultdict(int)
        ans = [0] * len(nums1)

        for i in range(len(nums1)):
            table[nums1[i]] = i

        print(table)


        for i in range(len(nums2)):
            if nums2[i] not in table:
                continue
            
            position = table[nums2[i]]
            val = -1
            for j in range(i, len(nums2)):
                if nums2[j] > nums2[i]:
                    val = nums2[j]
                    break
            
            ans[position] = val
        return ans
sol = Solution()
print(sol.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))