from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        max_profit = 0

        for p in prices:
            if p < min_buy:
                min_buy = p
            else:
                profit = p - min_buy
                max_profit = max(max_profit, profit)
        
        return max_profit

    
sol = Solution()
print(sol.maxProfit(prices = [7,1,5,3,6,4]))