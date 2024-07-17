from typing import List
import heapq as heap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        
        heap.heapify(stones)
        
        while len(stones)>1:
            #1st largest element
            s1 = heap.heappop(stones)
            #2nd largest element
            s2= heap.heappop(stones)
            
            if s1>s2:
                heap.heappush(stones,s1 - s2)
        
        stones.append(0)
                    
        return abs(stones[0])
    
res = Solution().lastStoneWeight([2,3,6,2,4])
res = Solution().lastStoneWeight([1,2])
res = Solution().lastStoneWeight([1,2])
print(res)