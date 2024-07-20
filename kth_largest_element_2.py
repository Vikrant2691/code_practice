from typing import List
import heapq
from collections import Counter
class Solution:
    
    
    # this is a solution with heap
    def findKthLargest_w_heap(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        while len(nums)>k:
            heapq.heappop(nums)
            
        return nums[0]
    
        
        

res = Solution().findKthLargest([2,3,1,5,4],2)
print(res)
            