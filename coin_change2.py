from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
            #cols                   rows
        dp = [[0] * (amount+1) for i in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1

        for c in range(len(coins)-1,-1,-1):
            for a in range(1,amount+1):
                dp[c][a] = dp[c+1][a]
                if a-coins[c]>=0:
                    dp[c][a] += dp[c][a-coins[c]]

        return dp[0][amount]
    

print(Solution().change(4,[1,2,3]))