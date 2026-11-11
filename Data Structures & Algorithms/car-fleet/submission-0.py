import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)

        stack = [-math.inf]
        for p, s in pairs:
            t = (target - p) / s
            if stack[-1] < t:
                stack.append(t)

        return len(stack) - 1
        