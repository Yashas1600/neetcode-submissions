# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count= 0
        def dfs(cur, curMax):
            if not cur:
                return 0
            if cur.val >= curMax:
                self.count += 1
            curMax = max(cur.val, curMax)
            dfs(cur.left,curMax)
            dfs(cur.right,curMax)  
        
        dfs(root,float("-inf")) 
        return self.count  
            
        