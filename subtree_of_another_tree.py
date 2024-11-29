from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.isMatching(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
    def isMatching(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.isMatching(root.left,subRoot.left) and self.isMatching(root.right,subRoot.right)
        
        return False


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
        

tree = Solution().create_tree([1,1])
subTree = Solution().create_tree([1])

print(Solution().isSubtree(tree,subTree))