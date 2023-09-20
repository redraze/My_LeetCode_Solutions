class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i, val in enumerate(prices[0:len(prices) - 1]):
            diff = prices[i + 1] - val
            if diff > 0:
                profit += diff
        return profit
