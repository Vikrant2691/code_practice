from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for interval in intervals:
            if newInterval[1]>=interval[0]:
                res.append([min(interval[0],newInterval[0]),max(interval[1],newInterval[1])])
            else:
                res.append(interval)
            
        return res
    
print(Solution().insert([[1,3],[4,6]],[2,5]))
print(Solution().insert([[1,2],[3,5],[9,10]],[6,7]))
        