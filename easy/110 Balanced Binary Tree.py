# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)

        if abs(lh - rh) > 1 : return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
        if root == None: return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
