class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ''
        
        res = (0,0)
        i=0
        
        for i in range(len(s)):
            l=r=i
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                
                if r-l > res[1]-res[0]:
                    res = (l,r)
            
                l-=1
                r+=1
                
        for i in range(len(s)):
            l=i
            r=i+1
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                
                if r-l > res[1]-res[0]:
                    res = (l,r)
            
                l-=1
                r+=1
        
        return s[res[0]:res[1]+1]

# print(Solution().longestPalindrome('ababd'))            
# print(Solution().longestPalindrome('abbd'))            
print(Solution().longestPalindrome('bb'))            