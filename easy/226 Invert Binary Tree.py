# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: return None
        l_inv = self.invertTree(root.left)
        r_inv = self.invertTree(root.right)
        root.left = r_inv
        root.right = l_inv

        return root