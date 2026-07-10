class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)

        for i in range(n):
            buy = prices[i]

            for j in range(i + 1, n):
                sell = prices[j]
                profit = sell - buy
                res = max(res, profit)

        return res