from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if not cost:
            return 0 
        
        n0=cost[len(cost)-1]
        n1=0
        
        end = len(cost)-2
        
        while end>=0:
            temp = cost[end] + min(n0,n1)   
            n1 = n0
            n0 = temp
            end-=1
            
        return min(n0,n1)
    
res = Solution().minCostClimbingStairs([1,2,3])
print(res)