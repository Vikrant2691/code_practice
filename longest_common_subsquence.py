class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        
        rows=len(text1)
        cols=len(text2)
                
        dp = [[0 for c in range(cols+1)] for r in range(rows+1)]
        
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 +dp[r+1][c+1]
                else:    
                    dp[r][c] = max(dp[r][c+1],dp[r+1][c])
                
        return dp[0][0]
        
print(Solution().longestCommonSubsequence("bsbininm","bkjkv"))