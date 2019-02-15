# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        res = []
        self.helper(root, 0 , res)
        for cur in res:
            for i in range(len(cur)-1):
                cur[i].next = cur[i+1]

    def helper(self, root, level, res):
        if not root: return
        if len(res) < level+1:
            res.append([])
        res[level].append(root)
        self.helper(root.left, level+1, res)
        self.helper(root.right, level+1, res)