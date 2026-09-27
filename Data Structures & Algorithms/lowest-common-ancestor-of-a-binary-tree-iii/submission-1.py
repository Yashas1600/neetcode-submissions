"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        hashSet = set()
        while p:
            hashSet.add(p)
            p = p.parent
        while q not in hashSet:
            q = q.parent
        return q
        
        