from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s)+1)
        dp[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if i+len(w)<len(dp) and s[i:i+len(w)]==w:
                    dp[i]= dp[i] or dp[i+len(w)]
                # if dp[i]:
                    # break

        return dp[0]
    
print(Solution().wordBreak("neetcode",["neet","code"]))
print(Solution().wordBreak("applepenapple",["apple","pen","ape"]))
print(Solution().wordBreak("catsincars", ["cats","cat","sin","in","car"]))
print(Solution().wordBreak("abcd", ["a","abc","b","cd"]))