# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(l1, r1, l2, r2):
            if l1 > r1: return None
            root = TreeNode(preorder[l1])
            i, j = l1, l2
            while inorder[j] != preorder[l1]:
                i += 1
                j += 1
            root.left = build(l1+1, i, l2, j)
            root.right = build(i+1, r1, j+1, r2)
            return root
        return build(0, len(preorder)-1, 0, len(inorder)-1)