# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def getHeight(root: TreeNode):
            if not root: return 0
            lh = getHeight(root.left)
            rh = getHeight(root.right)
            return lh + 1 if lh >= rh else rh + 1

        self.res = 0
        def getAns(root):
            if not root: return
            self.res = max(self.res, getHeight(root.left) + getHeight(root.right))
            getAns(root.left)
            getAns(root.right)

        getAns(root)
        return self.res

'''
best Answer 
class Solution:
    def __init__(self):
        self.ans = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.depth(root)
        return self.ans
        
    def depth(self,root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        if left+right > self.ans:
            self.ans = left+right
        return 1+max(left,right)

'''
