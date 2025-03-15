from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def dfs(node:Optional[TreeNode],left,right) -> bool:
            if not node:
                return True
            
            if left>root.val>right:
                return False
            
            return dfs(node,left,node.val) and dfs(node,node.val,right)
            
        return dfs(root,float('-inf'),float('inf'))