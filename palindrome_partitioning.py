from typing import List

class Solution:
    
    def partition(self, s: str) -> List[List[str]]:
        
        res,part= [],[]
        
        def is_palindrome(l,r) -> bool:
            while l<r:
                if r<len(s) and s[l] != s[r]:
                    return False 
                l+=1
                r-=1
            return True
        
        def backtrack(i):
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if is_palindrome(i,j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
                              
                
        backtrack(0)
        
        return res

print(Solution().partition("aab"))