class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for sellPrice in prices:
            profit = sellPrice - minBuy
            maxProfit = max(maxProfit, profit)
            minBuy = min(minBuy, sellPrice)
        return maxProfit