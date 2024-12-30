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
        
        def bfs(node:Optional[TreeNode],root_val:int,sub_tree:int) -> bool:
            if not node:
                return True
            
            if sub_tree == 0 and node.val>root_val:
                return False
             
            if sub_tree == 1 and node.val<root_val:
                return False
            
            return bfs(node.left,root.val,0) and bfs(node.right,root.val,1)
            
        return bfs(root.left,root.val,0) and bfs(root.right,root.val,0)