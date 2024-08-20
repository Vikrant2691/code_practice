from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0]*len(temperatures)
        for i,v in enumerate(temperatures):
            
            while stack and stack[-1][1]<v:
                index,value = stack.pop()
                res[index]=i-index
            stack.append((i,v))
        
        return res
    

print(Solution().dailyTemperatures([30,38,30,36,35,40,28]))