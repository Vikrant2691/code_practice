from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res =[0] * n
        prefix_arr=[0] * n
        postfix_arr=[0] * n
        
        prefix_arr[0] = postfix_arr[n-1] = 1
        
        for i in range(1,n):
            prefix_arr[i]=nums[i-1]*prefix_arr[i-1]
        for i in range(n-2,-1,-1):
            postfix_arr[i]=nums[i+1]*postfix_arr[i+1]
        for i in range(n):
            res[i]=prefix_arr[i]*postfix_arr[i]
            
        return res
            
print(Solution().productExceptSelf([1,2,4,6]))