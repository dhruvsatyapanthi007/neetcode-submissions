class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            res = max(res, area)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return res
        