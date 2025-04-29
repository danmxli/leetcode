from typing import List
import math


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        def search(i: int, j: int, k: int) -> int:
            # find kth smallest element in merged array
            # i and j are respective indicies of nums1 and nums2
            # k is median position in combined array

            # base case
            if i >= m:
                # exhausted nums1
                return nums2[j+k-1]
            if j >= n:
                # exhausted nums2
                return nums1[i+k-1]
            if k == 1:
                # second smallest element in merged array reached
                return min(nums1[i], nums2[j])

            # recursive case
            # select middle element position from remaining elements
            p = k // 2
            # use infinity for element with index out of bounds
            e1 = nums1[i+p-1] if (i+p-1 < m) else math.inf
            e2 = nums2[j+p-1] if (j+p-1 < n) else math.inf

            if e1 < e2:
                return search(i+p, j, k-p)
            else:
                return search(i, j+p, k-p)

        # driver
        lower_median = search(0, 0, (n+m+1)//2)
        upper_median = search(0, 0, (n+m+2)//2)
        return (lower_median + upper_median) / 2