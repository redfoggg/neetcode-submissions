class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy, maxProfit = prices[0], 0

        for p in prices:
            maxProfit = max(maxProfit, p - minBuy)
            minBuy = min(minBuy, p)


        return maxProfit





        