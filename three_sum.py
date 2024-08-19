from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0,len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1,len(nums)-1            
            while l < r:
                sum = nums[i]+nums[l]+nums[r]
                if sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    
                if sum < 0:
                    l+=1
                if sum > 0:
                    r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
        
        return res

print(Solution().threeSum([-1,0,1,2,-1,-4]))   
print(Solution().threeSum([0,1,1]))   
print(abs(1)) 
            