from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return [[]]
        
        candidates.sort()
        
        result = []
        subset = []
        
        #this solution works on the principle of inclusion and exclusion
        #e.g. [1,2,3,4] and target is 7 
        # we can include 1 or exclude 1, hence the backtracking step
        # Moreover to exclude dups we can sort the array and excluding it form the backtracking subset on line no.28
        
        def dfs(i,sum):
            
            #add to result subset
            if sum == target:
                result.append(subset.copy())
                return
            
            #not a result subset
            if sum > target or i>=len(candidates):
                return
            
            #include a candidate
            subset.append(candidates[i])
            dfs(i+1,sum+candidates[i])
            
            #inc till the dups are ignored
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            
            #exclude a candidate
            subset.pop()
            dfs(i+1,sum)
            
        dfs(0,0)
        
        return result
        
res = Solution().combinationSum2([9,2,2,4,6,1,5],8)

print(res)