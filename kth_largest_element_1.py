from typing import List
import heapq as heap

class KthLargest:
    
    h=[]
    k=0  

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums.copy()
        heap.heapify(self.h)
        

    def add(self, val: int) -> int:
        
        heap.heappush(self.h,val)
        while self.k<len(self.h):
            heap.heappop(self.h)
        
        return self.h[0]
        
kthLargest = KthLargest(1, [])
# kthLargest = KthLargest(3, [1, 2, 3, 3])
print(kthLargest.add(3))   # return 3
print(kthLargest.add(-2))   # return 3
print(kthLargest.add(5))   # return 3
print(kthLargest.add(10))   # return 3
print(kthLargest.add(9))   # return 3
# print(kthLargest.add(5))   # return 3
# print(kthLargest.add(6))   # return 3
# print(kthLargest.add(7))   # return 5
# print(kthLargest.add(8))