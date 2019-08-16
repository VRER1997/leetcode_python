# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res, self.cnt = 0, 0
        def inOrder(root:TreeNode):
            if not root:
                return
            if self.cnt > k:
                return
            inOrder(root.left)
            self.cnt += 1
            if self.cnt == k:
                self.res = root.val

        inOrder(root)

        return self.res