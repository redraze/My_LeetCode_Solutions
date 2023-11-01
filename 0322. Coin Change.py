class Solution:
    # Solution 2: tabulation
    def coinChange(self, coins: List[int], amount: int) -> int:
        tab = [0] + [float('inf')] * (amount)

        coins = [coin for coin in coins if coin <= amount]
        coins = sorted(coins)

        for coin in coins:
            for i in range(coin, amount + 1):
                tab[i] = min(tab[i], tab[i - coin] + 1)

        if tab[-1] == float('inf'):
            return -1
        return tab[-1]

    # # Solution 1: recursion with memory cache
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     if amount == 0:
    #         return 0 

    #     # minimize sort time by eliminating un-usable coins beforehand
    #     coins = [coin for coin in coins if coin <= amount]
    #     coins = sorted(coins)

    #     if not coins or coins[0] > amount:
    #         return -1

    #     def dp(coins: List[int], amount: int) -> int:
    #         if amount in cache:
    #             return cache[amount]

    #         # limit list comprehension sizes in future recursions
    #         coins = coins.copy()
    #         while coins and coins[-1] > amount:
    #             coins.pop()
    #         if not coins:
    #             return float('inf')

    #         cache[amount] = min([
    #             1 + dp(coins, amount - coin) for coin in coins[::-1]
    #         ])

    #         return cache[amount]
        
    #     cache = {0: 0}
    #     dp(coins, amount)
        
    #     if cache[amount] == float('inf'):
    #         return -1
    #     return cache[amount]
