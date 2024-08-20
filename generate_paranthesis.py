from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def add_permutation(str:List,o:int,c:int):
            
            if o==n and c==n:
                res.append(''.join(str))
                return
            
            if o<n:
                str.append('(')
                add_permutation(str,o+1,c)
                str.pop()
                
            if c<o and c<n:
                str.append(')')
                add_permutation(str,o,c+1)
                str.pop()
        
        add_permutation([],0,0)
        return res
        
print(Solution().generateParenthesis(3))