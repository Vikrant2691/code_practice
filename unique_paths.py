class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m==n==0:
            return 0
        if m==0 or n==0:
            return 1
        
        dp =[[0 for c in range(n)] for r in range(m)]
        
        for r in range(0,len(dp)):
            dp[r][0] = 1
        for c in range(1,len(dp[0])):
            dp[0][c] = 1
            
        for r in range(1,len(dp)):
            for c in range(1,len(dp[0])):
                dp[r][c] = dp[r-1][c]+dp[r][c-1]
        
        return dp[m-1][n-1]

print(Solution().uniquePaths(1,1))