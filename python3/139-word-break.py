from typing import List
from collections import deque

# intuition: bfs approach
# check if it can traverse to the end of the string
# use nodes as indicies to track substrings
# can move to the next node if the substring of s exists in wordDict
# CAN ALSO DO THIS USING DP

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        q = deque([0])
        seen = set()

        while q:
            curr = q.popleft()

            # reached the end of s
            if curr == len(s):
                return True
            
            # adjacent exploration
            for end in range(curr+1, len(s)+1):
                # optimization
                if end in seen:
                    continue

                # substring condition
                if s[curr:end] in word_set:
                    seen.add(end)
                    q.append(end)

        
        # exhausted all options
        return False