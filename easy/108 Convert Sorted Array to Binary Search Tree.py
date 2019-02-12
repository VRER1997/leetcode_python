# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.generateTree(nums, 0, len(nums)-1)

    def generateTree(self, nums, l, r):
        if l > r:
            return None
        mid = (l+r)//2
        root = TreeNode(nums[mid])
        root.left = self.generateTree(nums, l, mid-1)
        root.right = self.generateTree(nums, mid+1, r)

        return root

if __name__ == '__main__':
    s = Solution()
    s.generateTree([-10,-3,0,5,9])


