class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minb, maxs = prices[0], 0

        for p in prices:
            maxs = max(maxs, p - minb)
            minb = min(minb, p)

        return maxs

        