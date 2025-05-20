from typing import List
import math

# TODO: see general binary search templates

# piles[i] represents the quantity of bananas 
# compute the time as ceil(piles[i]/k)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # formula to compute time to eat all bananas
        def time(piles: List[int], speed: int) -> int:
            t = 0
            for item in piles:
                t += math.ceil(item/speed)
            return t
        
        # define search space from 1 to max of piles
        left = 1
        right = max(piles)

        while left < right:
            ...
            # not using indices
            mid = left + (right - left) // 2
            t = time(mid)

            if t <= h:
                right = mid
            else:
                left = mid+1
        
        return left