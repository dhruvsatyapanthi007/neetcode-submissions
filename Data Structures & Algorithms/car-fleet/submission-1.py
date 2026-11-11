import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)

        res = [-math.inf]

        for p, s in pairs:
            t = (target - p) / s
            if res[-1] < t:
                res.append(t)

        return len(res) - 1
        