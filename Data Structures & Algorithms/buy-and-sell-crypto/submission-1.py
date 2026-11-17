class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = float('inf')
        for price in prices:
            minPrice = min(minPrice, price)
            res = max(res, price - minPrice)

        return res
