from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for n in nums:
            if n in table:
                return True
            table[n] = 1
        
        return False