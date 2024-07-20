from collections import Counter
from collections import deque
from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # number of tasks matter... more frequent task taken 1st would be efficient
        # add add the tasks to hm as => ['A']->2
        # the 'values' to heap (to get the frequent ones first)
        # now we have an interval that starts from 1,2,3,...
        # for every interval we pop the heap top process the task (decrement by 1) -> x
        # we add this task to a queue to as (current quant of task (x), cool_off+interval)
        # this will repeat till the heap or q are empty
        
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        q=deque()
        time = 0
        
        while max_heap or q:
            time +=1
            
            if max_heap:
                #process the task
                cnt = 1+heapq.heappop(max_heap)
                if cnt:
                    #add the process and next interval to a q
                    q.append([cnt,time+n])
            
            # check if the process time matches the current time
            if q and q[0][1]==time:
                # add to heap, ready for processing
                heapq.heappush(max_heap,q.popleft()[0])
                    
        return time
    
res = Solution().leastInterval(["A","A","A","B","C"],3)
print (res)