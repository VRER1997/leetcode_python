# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        remains = [i for i in range(1,n+1)]
        def getAns(remains):
            if not remains:
                return [None]
            res = []
            for idx, num in enumerate(remains):
                for l in getAns(remains[:idx]):
                    for r in getAns(remains[idx + 1:]):
                        node = TreeNode(num)
                        node.left = l
                        node.right = r
                        res.append(node)
            return res

        #print(remains)
        return getAns(remains)

if __name__ == '__main__':
    s = Solution()
    s.generateTrees(3)
