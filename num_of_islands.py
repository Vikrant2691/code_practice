from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        num_of_islands = 0

        if not grid:
            return 0
        
        def dfs(r, c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]=='0':
                return 
            
            grid[r][c]='0'

            dfs(r+1, c)
            dfs(r-1, c)  
            dfs(r, c+1)
            dfs(r, c-1)
            
        def bfs(r,c):
            q = deque()
            directions= [[1,0],[-1,0],[0,1],[0,-1]]
            grid[r][c]='0'
            q.append((r,c))
            
            while q:
                row , col = q.popleft() 
                
                for dr, dc in directions:
                    nr =row+dr
                    nc =col+dc
                    if nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == '1':
                        grid[nr][nc]='0' 
                        q.append((nr,nc))
        
        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c]=='1':
                    bfs(r, c)
                    num_of_islands += 1
        return num_of_islands
        

grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]

res = Solution().numIslands(grid)

print(res)