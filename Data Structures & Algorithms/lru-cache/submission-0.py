import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.lru:
            self.lru.move_to_end(key, last=True)
            return self.lru[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.lru[key] = value
        self.lru.move_to_end(key, last=True)

        if len(self.lru) == self.capacity + 1:
            self.lru.popitem(last=False)
