from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent_w_heap(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        list = [(-v,k) for k,v in counts.items()]
        heapq.heapify(list)
        res = []
        i=0
        while i < k:
            res.append(heapq.heappop(list)[1])
            i+=1
        return res
    
    # there is one more solution where we can use bucket sort
    # here we will have array with count,[list of number having that count]
    # so if 1 occurs 1 time and 2, 3 times.. the array will have 0->[],1->[1],2->[],3->[2]
    def topKFrequent(self, nums: List[int], k: int) -> int:
        #get counts num->count
        counts = Counter(nums)
        #create an array of size len(nums)
        freq = [[]for i in range(len(nums)+1)]
        # for each k, v in counts arr[v].append(k)
        for key,v in counts.items():
            freq[v].append(key)
        #start from the end, for each count add to res array
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res            
        
        
res = Solution().topKFrequent([1,2,2,3,3,3],2)
print(res)