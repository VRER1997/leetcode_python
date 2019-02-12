# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        lh = self.minDepth(root.left)
        rh = self.minDepth(root.right)

        return  (lh+rh+1) if (lh == 0 or rh == 0) else min(lh, rh)+1
