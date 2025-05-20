# intuition
# use binary search to build the count of complete rows
# check if any remaining coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        count = 0

        while left <= right:
            mid = (left + right) // 2

            # using n(n+1)/2
            if mid * (mid+1) // 2 <= n:
                left = mid+1

            else:
                right = mid-1

        return right