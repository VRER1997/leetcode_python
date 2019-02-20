# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self.pushAllLeft(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.hasNext():
            cur = self.stack.pop()
            if cur.right:
                self.pushAllLeft(cur.right)
            return cur.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.stack != []

    def pushAllLeft(self, node):
        cur = node
        while cur:
            self.stack.append(cur)
            cur = cur.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()