# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        okay so the strat is to pass a list with [withroot,without root] for every subtree
        then withroot = root + root.left(without root) + roo.rright(without root) or index[1]
        then without root = max(root.left) + max(root.right)
        """
        def dfs(node):
            if not node:
                return [0,0]

            leftPair = dfs(node.left)
            rightPair = dfs(node.right)

            withRoot = node.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]

        return max(dfs(root))



            