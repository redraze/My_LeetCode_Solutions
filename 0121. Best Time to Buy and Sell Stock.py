class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = prices[0]
        for i, val in enumerate(prices):
            if val < min:
                min = val
            elif val - min > profit:
                profit = val - min
        return profit
