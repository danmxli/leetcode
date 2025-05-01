from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_avg = 0
        count = 0

        # first window
        for i in range(0, k):
            window_avg += arr[i] / k
        if window_avg >= threshold:
            count += 1

        for i in range(k, len(arr)):
            window_avg += (arr[i] / k) - (arr[i-k] / k)
            if window_avg >= threshold:
                count += 1
        
        return count

sol = Solution()
print(sol.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))