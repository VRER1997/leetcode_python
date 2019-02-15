# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def build(l1, r1, l2, r2):
            if l1 > r1:
                return None
            root = TreeNode(postorder[r2])
            i, j = r1, r2
            while inorder[i] != postorder[r2]:
                i -= 1
                j -= 1
            root.left = build(l1, i-1, l2, j-1)
            root.right = build(i+1, r1, j, r2-1)
            return root

        return build(0, len(inorder)-1, 0, len(postorder)-1)