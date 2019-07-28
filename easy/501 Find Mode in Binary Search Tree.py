# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        dic = {}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val not in dic:
                dic[node.val] = 1
            dic[node.val] += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        res = []
        max_ele = max(dic.values())
        for key, val in dic.items():
            if val == max_ele:
                res.append(key)
        return res


