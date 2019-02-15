# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.ret = []
        def preOrder(root):
            if root:
                self.ret.append(root)
                if root.left:
                   preOrder(root.left)
                if root.right:
                    preOrder(root.right)
        preOrder(root)
        for index, node in enumerate(self.ret):
            node.left = None
            node.right = self.ret[index+1] if index + 1 < len(self.ret) else None
        return self.ret[0]