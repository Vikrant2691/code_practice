from typing import List
import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hm = {}
        
        for i in range(0,len(position)):
            hm[position[i]] = speed[i]
            
        position.sort()
        
        time = [0]*len(position)
        for i in range(0,len(position)):
            time[i] = (target-position[i])/hm[position[i]]
            
        count = len(time)
        
        for i in range(len(time)-1,0,-1):
            if time[i]>=time[i-1]:
                count-=1
                time[i-1]=time[i]
        
        return count            

print(Solution().carFleet(10,[4,1,0,7],[2,2,1,1]))
print(Solution().carFleet(10,[1,4],[3,2]))
print(Solution().carFleet(10,[6,8],[3,2]))
print(Solution().carFleet(10,[0,4,2],[2,1,3]))