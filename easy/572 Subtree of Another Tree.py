# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def is_same(s: TreeNode, t: TreeNode):
            if not s and not t: return True
            if not s and t: return False
            if s and not t: return False
            return is_same(s.left, t.left) and is_same(s.right, t.right) and s.val == t.val

        if not s and not t: return True
        if not s and t: return False
        return is_same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)