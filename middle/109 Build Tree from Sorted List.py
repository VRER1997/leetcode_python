# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def sortedArrayToBST(nums):
            if not nums:
                return None

            mid = len(nums)// 2
            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(nums[:mid])
            root.right = sortedArrayToBST(nums[mid+1:])
            return root

        if not head: return None
        else:
            lst = []
            while head:
                lst.append(head.val)
                head = head.next
            return sortedArrayToBST(lst)


