from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        
        while l<=r:
            mid = int((l+r)/2)
            
            if nums[mid]==target:
                return mid
            
            if nums[l]<=nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if target < nums[mid] or target > nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        
        return -1
    
# print(Solution().search([3,4,5,6,1,2],1))
# print(Solution().search([3,5,6,0,1,2],4))
print(Solution().search([5,1,3],5))