# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        we can up left right
        can't repeat nodes or retraverse them
        """
        res = [root.val]
        def dfs(node):
            if not node:
                return 0
            #postorder
            left = dfs(node.left)
            left = max(0,left)
            right = dfs(node.right)
            right = max(0,right)
            #with split 
            res[0] = max(res[0],left + right + node.val)
            return node.val + max(left, right)
        dfs(root)
        return res[0]            
        