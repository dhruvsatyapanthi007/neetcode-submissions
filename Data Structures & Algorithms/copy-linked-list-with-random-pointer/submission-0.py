"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old2New = {}
        new2Old = {}

        curr = head
        newHead = Node(-1)
        newCurr = newHead
        while curr:
            newCurr.next = Node(curr.val)
            newCurr = newCurr.next
            old2New[curr] = newCurr
            new2Old[newCurr] = curr
            curr = curr.next

        newHead = newHead.next
        newCurr = newHead
        while newCurr:
            if new2Old[newCurr].random:
                newCurr.random = old2New[new2Old[newCurr].random]
            newCurr = newCurr.next

        return newHead
