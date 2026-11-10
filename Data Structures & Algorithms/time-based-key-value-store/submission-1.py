class TimeMap:

    def __init__(self):
        self.mapping = collections.defaultdict(lambda: [("", -1)])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.mapping[key]
        left = 0
        right = len(pairs) - 1

        while left <= right:
            mid = (left + right) // 2

            if pairs[mid][1] == timestamp:
                return pairs[mid][0]
            elif pairs[mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return pairs[right][0]
