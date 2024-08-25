class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        
        max_len = 0
        l=r=0
        
        h_set = set()
        while r<len(s):
            if s[r] in h_set:
                h_set.remove(s[l])
                l+=1
            else:
                h_set.add(s[r])
                max_len=max(max_len,(r-l)+1)
                r+=1
 
        return max_len
    
print(Solution().lengthOfLongestSubstring("zxyzxyz"))
print(Solution().lengthOfLongestSubstring("xxxx"))