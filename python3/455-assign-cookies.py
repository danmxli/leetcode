from typing import List

# intuition: greedy approach
# sort both arrays
# give the smallest cookie first

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g) 
        s = sorted(s)

        # modified two pointer approach
        i = 0
        j = 0

        while i < len(g) and j < len(s):
            # condition to assign cookie
            if s[j] >= g[i]:
                i += 1
            j += 1

        return i