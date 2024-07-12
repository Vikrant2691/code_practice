from typing import List
from collections import deque

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0
        
        def bfs(grid, r, c) -> int:
            q = deque()
            dir = [[1,0],[-1,0],[0,1],[0,-1]]
            count = 0
            
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                
                row, col = q.popleft()
                count+=1
                
                for dr, dc in dir:
                    nr = row+dr
                    nc = col+dc
                    
                    if nr>=0 and nr<rows and nc>=0 and nc<cols and (nr,nc) not in visited and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        visited.add((nr,nc))
            
            return count
        
        for r in range(0,rows):
            for c in range(0,cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area,bfs(grid,r,c))
                    
        return max_area
        
        

grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]]

res = Solution().maxAreaOfIsland(grid)

print(res)