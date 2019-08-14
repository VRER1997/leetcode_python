# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.tem = 0
        def afterOrder(root: TreeNode):
            if not root: return
            afterOrder(root.right)
            self.tem += root.val
            root.val = self.tem
            afterOrder(root.left)
        afterOrder(root)
        return root




