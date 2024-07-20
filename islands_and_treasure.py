from typing import List
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        if not grid:
            return
        
        def bfs(grid,r,c,visited):
            
            q = deque()
            q.append((r,c,grid[r][c]))
            
            while q:
                row,col,dist = q.popleft()
                visited.add((row,col))
                
                if grid[row][col]!=0:
                    grid[row][col]=min(grid[row][col],dist)
                    
                
                dir = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in dir:
                    nr = row + dr
                    nc = col + dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]>=0 and (nr,nc) not in visited:
                        q.append((nr,nc,1+dist))
                                     
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    visited = set()
                    bfs(grid,r,c,visited)
        
        print(grid)
        
Solution().islandsAndTreasure(grid=[[2147483647,2147483647,2147483647],[2147483647,-1,2147483647],[0,2147483647,2147483647]])