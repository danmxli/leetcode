from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # frequency count table
        table = {
            "b":0,
            "a":0,
            "l":0,
            "o":0,
            "n":0
        }

        for c in text:
            if c in table:
                table[c] += 1

        # handle "l" and "o"
        table["l"] = table["l"] // 2
        table["o"] = table["o"] // 2
        
        ans = float('inf')
        for k in table:
            ans = min(ans, table[k])
        return ans
    
sol = Solution()
print(sol.maxNumberOfBalloons(text = "loonbalxballpoon"))