
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode,max_val) -> int:
            if not root:
                return 0
            res = 1 if root.val>max_val else 0
            max_val = max(root.val,max_val)
            res += dfs(root.left,max_val)
            res += dfs(root.right,max_val)
        
        return dfs(root,0)

root = create_tree([2,1,1,3,None,1,5])
print(Solution().goodNodes(root))
