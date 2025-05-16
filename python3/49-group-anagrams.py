from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(int)

        # first pass, maps key to answer index
        index = 0
        for st in strs:
            l = list(st)
            l.sort()
            key = ''.join(l)
            
            if key not in table:
                table[key] = index
                index += 1

        # pythonic way of building a 2D matrix
        ans = [[] for _ in range(index)]
        # second pass to build the answer
        for st in strs:
            l = list(st)
            l.sort()
            key = ''.join(l)

            ans[table[key]].append(st)

        return ans
    
sol = Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))