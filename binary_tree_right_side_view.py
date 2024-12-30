from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def bfs(root,level):
            if not root:
                return
            if len(res)<=level:
                res.append(root.val)
            else:
                res[level] = root.val
            
            bfs(root.left,level+1)
            bfs(root.right,level+1)
            
        bfs(root,0)
        
        return res
    
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
    
tree = create_tree([1,2,3,4,None,None,5,6])

print(Solution().rightSideView(tree))