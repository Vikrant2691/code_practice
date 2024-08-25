from typing import List
import sys
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r=0,len(nums)-1
        
        res = -1
        
        while l<r:
            mid = int((l+r)/2)
            
            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]<nums[r]:
                r=mid-1
            elif nums[mid]==target:
                return mid
        
        return nums[l] if nums[l]==target else -1
    
print(Solution().search([3,4,5,6,1,2],1))