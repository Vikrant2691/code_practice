from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return [[]]
        
        # the technique is to treat the array as a subproblem 
        # for e.g. result for [1,2,3] will be solution of subproblem [2,3] and subsequently [3]
        # [3] -> [[3]], then by adding 2 to [3] -> [[2,3],[3,2]], i.e. adding 2 at the front and back
        # in other words, adding 2 at each position
        
        #1 create a subproblem by removing 1st element
        perms = self.permute(nums[1:])
        result=[]
        
        #2 for each value in current permutation like [3] 
        for p in perms:
            #3 add current nums[0](2 in this case) at ith position
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                #4 insert the current list to result in our case [2,3] for i=0
                result.append(p_copy)
        
        return result
        
        
res = Solution().permute([1,2,3])

print(res)