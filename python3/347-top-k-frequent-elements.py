from typing import List
from collections import defaultdict
import heapq

# intuition:
# return the K most frequent items
# create table - key is itemid, occurrences is value
# use a max pq to get the K highest occurences

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)
        for n in nums:
            table[n] += 1

        pq = []
        for key in table:
            heapq.heappush(pq, (-table[key], (key)))
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(pq)[1])

        return ans

sol = Solution()
print(sol.topKFrequent(nums = [-1,-1], k = 1))