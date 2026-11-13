# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseHead = ListNode(-1)
        curr = head

        while curr is not None:
            nextNode = curr.next
            curr.next = reverseHead
            reverseHead = curr
            curr = nextNode

        if head:
            head.next = None
        else:
            reverseHead = None

        return reverseHead
        