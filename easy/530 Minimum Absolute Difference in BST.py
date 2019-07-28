# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        lst = []

        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            lst.append(root.val)
            inorder(root.right)

        inorder(root)
        res = lst[-1] - lst[0]
        for i in range(len(lst)-1):
            res = min(res, lst[i+1]-lst[i])

        return res