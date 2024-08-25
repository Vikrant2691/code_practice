from typing import List
import sys

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r=0,len(nums)-1
        min_val = sys.maxsize
        while l<r:
            mid = int((l+r)/2)
            min_val = min(min_val,nums[mid])
            
            if nums[mid]>=nums[r]:
                l=mid+1
            else:
                r=mid-1
            
        return min(nums[l],min_val)
                          
                
            
# print(Solution().findMin([3,4,5,6,1,2]))
# print(Solution().findMin([4,5,0,1,2,3]))
print(Solution().findMin([4,5,6,7]))