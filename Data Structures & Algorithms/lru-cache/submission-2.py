class ListNode:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.maxCapacity = capacity
        self.currCapacity = 0
        self.nodeMap = {}
        self.head = ListNode(-1, -1)
        self.tail = self.head

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            self.makeKeyMostRecentlyUsed(key)
            return self.nodeMap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.nodeMap:
            if self.currCapacity == self.maxCapacity:
                self.deleteLeastRecentlyUsedKey()
            else:
                self.currCapacity += 1

            self.tail.next = ListNode(key, value, self.tail)
            self.tail = self.tail.next
            self.nodeMap[key] = self.tail
        else:
            self.makeKeyMostRecentlyUsed(key)
            self.nodeMap[key].value = value

    def makeKeyMostRecentlyUsed(self, key):
        curr = self.nodeMap.get(key)
        if curr and curr != self.tail:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.tail.next = curr
            curr.prev = self.tail
            curr.next = None
            self.tail = curr

    def deleteLeastRecentlyUsedKey(self):
        curr = self.head.next
        if curr:
            del self.nodeMap[curr.key]
            if curr != self.tail:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            else:
                curr.prev.next = None
                self.tail = curr.prev
