# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        given root
        insert val in bst
        return root

        step 1: find the place to insert:
        so cur = cur.left if if val < cur.val
        opppsotire from right if neither this is the spot
        maintain a prev pointer 


        then second part is fixing the rest of the tree



        cases where there is no right og left subtree 
        then case where ther is one and 
        case where there is both 
        """


        if not root:
            return TreeNode(val)
        prev = None
        cur = root
        while cur:
            prev = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if val < prev.val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
        return root
                

            
