from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        visited = set()
        fresh = 0
        q = deque()
        time = 0
        #Multi Source BFS
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c,0)) 
        
        while q:
            r,c,t = q.popleft()
            time = max(time,t)
                
            dir=[[0,1],[0,-1],[1,0],[-1,0]]
            
            for row,col in dir:
                nr = r+row
                nc = c+col
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1 and (nr,nc) not in visited:
                    q.append((nr,nc,t+1))
                    visited.add((nr,nc))
                    fresh-=1
                    grid[nr][nc]=2
    
        
        return time if fresh==0 else -1 
    

print(Solution().orangesRotting([[1,1,0],[0,1,1],[0,1,2]]))
print(Solution().orangesRotting([[1,0,1],[0,2,0],[1,0,1]]))