from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #base case
        if not root:
            return
      
        #create a new node
        new_root = TreeNode()
       
        new_root.val = root.val
        #assign rhs to lhs
        new_root.left = self.invertTree(root.right)
        #assign lhs to rhs
        new_root.right = self.invertTree(root.left)
        
        return new_root
       