from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        
        l,r=0,1
        max_profit = 0
        while r<len(prices):
            if prices[r]<prices[l]:
                l=r
            else:
                max_profit = max(max_profit,prices[r]-prices[l])
            r+=1
            
        return max_profit
        
print(Solution().maxProfit([10,8,7,5,2]))
print(Solution().maxProfit([10,1,5,6,7,1]))
print(Solution().maxProfit([7,1,5,3,6,4]))
            
        