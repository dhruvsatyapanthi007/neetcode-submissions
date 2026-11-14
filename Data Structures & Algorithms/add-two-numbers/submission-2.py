# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()

        c = 0
        curr = res
        while l1 and l2:
            s = l1.val + l2.val + c
            c = s // 10
            curr.next = ListNode(s % 10)

            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        l = l1 or l2
        while l:
            s = l.val + c
            c = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next
            l = l.next

        if c:
            curr.next = ListNode(c)

        return res.next
        