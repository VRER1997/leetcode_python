# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None: return False
        if root.val == sum and root.left == None and root.right == None: return True
        res = False
        if root.left != None:
            res = res or self.hasPathSum(root.left, sum-root.val)
        if root.right != None:
            res = res or self.hasPathSum(root.right, sum-root.val)

        return res
