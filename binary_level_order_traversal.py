from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.traverse_levels(root,0,res)
        return res
        
    def traverse_levels(self, root, level,res):
        if not root:
            return None
        
        if len(res) == level:
            res.append([])
            
        res[level].append(root.val)
        
        self.traverse_levels(root.left,level+1,res)
        self.traverse_levels(root.right,level+1,res)
        
def create_tree(elements) -> TreeNode:
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
    
tree = create_tree([1,2,3,4,5,6,7])

print(Solution().levelOrder(tree))