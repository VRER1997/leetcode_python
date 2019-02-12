"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root : return []
        ret, cur = [], [root]
        while cur:
            next, temp = [], []
            for node in cur:
                temp.append(node.val)
                next += node.children
            ret.append(temp)
            cur = next
        return ret