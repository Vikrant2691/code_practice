from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        
        def dfs(r,c,wi):
            if wi>=len(word):
                return True
            
            if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or board[r][c]!=word[wi] or (r,c) in visited:
                return False
            
            visited.add((r,c))
            
            return dfs(r+1,c,wi+1) or dfs(r-1,c,wi+1) or dfs(r,c+1,wi+1) or dfs(r,c-1,wi+1)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==word[0]:
                    if dfs(r,c,0):
                        return True
                visited = set()
        
        return False

print(Solution().exist(board = [["C","A","A"],["A","A","A"],["B","C","D"]],
word = "AAB"))