from typing import List

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
        
        
        def helper(nums):
            
            
            rob1,rob2 = 0,0
            
            #rob1 -> value if we rob house n
            #rob2 -> value if we rob house n+1 and not n
            # recurrence relation -> max(nums[0]+rob[2..n],rob[1..n])
            
            for n in nums:
                temp = max(n+rob2,rob1)
                rob2 = rob1
                rob1 = temp
            
            return rob1
        
        return max(helper(nums[:len(nums)-1]),helper(nums[1:]))

res = Solution().rob([2,9,8,3,6])
print(res)

