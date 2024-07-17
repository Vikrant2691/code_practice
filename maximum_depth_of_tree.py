from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))    

def create_tree(list:List[int],i) -> Optional[TreeNode]:
    
    if i>=len(list):
        return
    
    root = TreeNode()
    root.val = list[i]
    root.left=create_tree(list, (2*i)+1)
    root.right=create_tree(list, (2*i)+2)
        
    return root
    
    
tree = [1,2,3,4,5,6,7]
root = create_tree(tree, 0)
res = Solution().maxDepth(root)
print(res)