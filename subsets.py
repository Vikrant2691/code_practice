from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #subset logic works on a trick of inclusion and exclusion
        #for subset [1,2,3] we can choose to include 1,that returns [1] or exclude 1
        #that returns empty set []. After including 1 we can then add the second element 2,
        #therefore our decision tree looks like this
        #       0
        #     /   \
        #   [1]    []
        #   /       \
        # [1,2]     [2]
        
        if not nums:
            return [[]]
        
        res = []
        
        subset = []
        
        
        def dfs(i):
            #i is level of the decision tree.. if i has reached the last element, 
            #it flushes to a result list
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            #add element to subset
            subset.append(nums[i])
        
            #add the next element by recursive call
            dfs(i+1)    
            #exclude the current element by by removing it from the subset
            subset.pop()
            #again add the next element by recursive call, this set will not have the current element
            dfs(i+1)
            
        dfs(0) 
        
        return res

res = Solution().subsets([1,2,3])

print(res)