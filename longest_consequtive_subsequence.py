from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        res = 0
        for n in nums:
            s.add(n)
            
        for n in nums:
            curr = n
            count = 0
            while curr in s:
                count+=1
                curr+=1
            res = max(res, count)
            
        return res

print(Solution().longestConsecutive([2,20,4,10,3,4,5]))
print(Solution().longestConsecutive([0,3,2,5,4,6,1,1]))
print(Solution().longestConsecutive([0]))
