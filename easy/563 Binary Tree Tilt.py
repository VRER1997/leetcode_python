# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.res = 0
        def find(root: TreeNode):
            if not root: return
            self.find(root.left)
            self.find(root.right)
            lsum, rsum = 0, 0
            if root.left:
                lsum = root.left.val
                root.val += root.left.val
            if root.right:
                rsum = root.right.val
                root.val += root.right.val
            self.res += abs(lsum - rsum)
            print(abs(lsum - rsum))

        find(root)
        return self.res


