from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        #subset logic works on a trick of inclusion and exclusion
        #for subset [1,2,3] we can choose to include 1,that returns [1] or exclude 1
        #that returns empty set []. After including 1 we can then add the second element 2,
        #therefore our decision tree looks like this
        #       0
        #     /   \
        #   [1]    []
        #   /       \
        # [1,2]     [2]
        # Now to handle duplicates we need ignore the recurring numbers.. so if the list is [1,2,3,2] 
        # we have to ignore second 2, if the list was [1,2,2,3], it would have been easier 
        # as we can ignore the adj nums that are same.
        # The soln is to sort the list and ignore the adj nums.
        
        if not nums:
            return [[]]
        
        nums.sort()
        
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
            
            #we will not add the next element in the exclude set.. bzc we have already included it in 1st set
            #while, not if bcz the there can be multiple duplicates not just 2
            while i+1<len(nums) and  nums[i]==nums[i+1]:
                i+=1
            
            #again add the next element by recursive call, this set will not have the current element
            dfs(i+1)
            
        dfs(0) 
        
        return res
            
res = Solution().subsetsWithDup([1,2,3])
res = Solution().subsetsWithDup([1,2,1])

print(res)