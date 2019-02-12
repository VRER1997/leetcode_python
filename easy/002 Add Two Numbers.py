# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        t = res
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            result = x + y + carry
            t.next = ListNode(result % 10)
            t = t.next

            carry = result // 10

            if l1 != None : l1 = l1.next
            if l2 != None : l2 = l2.next

        if carry > 0 :
            t.next = ListNode(1)

        return res.next


