from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        m_area = 0
        while l < r:
            area = (r-l) * (min(heights[l],heights[r]))
            m_area = max(m_area,area)

            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        
        return m_area
        
# print(Solution().maxArea([1,7,2,5,4,7,3,6]))
print(Solution().maxArea([2,2,2]))