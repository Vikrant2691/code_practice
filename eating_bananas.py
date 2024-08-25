from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def calculate_eat_time(limit)-> int:
            total_time=0
            for p in piles:
                total_time += (-(p//-limit))
            
            return total_time
        
        l,r = 1,max(piles)
        res =0
        while l<=r:
            mid = int((l+r)/2)
            eat_hrs = calculate_eat_time(mid)
            if eat_hrs<=h:
                res=mid
                r=mid-1
            if eat_hrs>h:
                l=mid+1
        return res
            
print(Solution().minEatingSpeed([1],9))
print(Solution().minEatingSpeed([25,10,23,4],4))