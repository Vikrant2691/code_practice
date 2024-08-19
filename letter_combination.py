from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        combinations = {}
        char_mapping = ['+','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        for i in range(0,len(char_mapping)):
            combinations[str(i)]=char_mapping[i]
          
        res= []
        def backtrack(i,part):
            if i>=len(digits):
                if part:
                    res.append(part)
                return
            str = combinations[digits[i]]
            for j in range(len(str)):
                part = part+str[j]
                backtrack(i+1,part)
                part=part[:-1]

        backtrack(0,'')
        return res
    
print(Solution().letterCombinations(""))