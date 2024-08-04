from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS,COLS = len(board),len(board[0])
        visited = set()
        
        def dfs(r,c,val):
            if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visited or board[r][c]=='X' or board[r][c]=='T':
                return
            
            visited.add((r,c))
            board[r][c]=val

            dfs(r+1,c,val)
            dfs(r-1,c,val)
            dfs(r,c+1,val)
            dfs(r,c-1,val)

        for r in range(ROWS):
            c=0
            if board[r][c]=='O':
                dfs(r,c,'T')
        
        for r in range(ROWS):
            c=COLS-1
            if board[r][c]=='O':
                dfs(r,c,'T')
        
        for c in range(COLS):
            r=0
            if board[r][c]=='O':
                dfs(r,c,'T')
        
        for c in range(COLS):
            r=ROWS-1
            if board[r][c]=='O':
                dfs(r,c,'T')
                
        visited=set()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='O' and(r,c) not in visited:
                    dfs(r,c,'X')
                if board[r][c]=='T':
                    board[r][c]='O'
                visited.add((r,c))
                
        print(board)

Solution().solve( [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
])