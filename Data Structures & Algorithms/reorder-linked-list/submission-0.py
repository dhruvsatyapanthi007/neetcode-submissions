# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        i = 0
        curr = head
        while i < (length + 1) // 2:
            i += 1
            curr = curr.next

        reverseSecondHalf = None
        while curr:
            nextNode = curr.next
            curr.next = reverseSecondHalf
            reverseSecondHalf = curr
            curr = nextNode

        curr = head
        while reverseSecondHalf:
            nextNode = curr.next
            curr.next = reverseSecondHalf
            reverseSecondHalf = reverseSecondHalf.next
            curr.next.next = nextNode
            curr = nextNode

        if curr:
            curr.next = None
