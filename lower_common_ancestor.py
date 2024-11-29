from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        
        
        
        return None
    

    def create_tree(self,elements) -> TreeNode:
        n=0
        def dfs(n):
            node = TreeNode(elements[n],None,None)
            if (2*n)+1<len(elements):
                node.left=dfs((2*n)+1)
            if (2*n)+2<len(elements):
                node.right=dfs((2*n)+2)
            return node   
        root = dfs(0)
        return root
    
    def traverse_tree(self,node:TreeNode):
        if not node:
            return None
        print(node.val)
        self.traverse_tree(node.left)
        self.traverse_tree(node.right)
        

root = Solution().create_tree([5,3,8,1,4,7,9,None,2])
Solution().traverse_tree(root)
