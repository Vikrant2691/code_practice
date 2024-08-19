class Solution:
    def isValid(self, s: str) -> bool:
        hm  = {}
        hm['{']='}'
        hm['(']=')'
        hm['[']=']'
        stack =[]
        for c in s:
            if c in '{([':
                stack.append(hm[c])
            else:
                if not stack or c !=stack[-1]:
                    return False
                stack.pop()
        
        return not stack
    
    
print(Solution().isValid('([{}]))'))
print(Solution().isValid('('))