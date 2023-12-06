class Solution:
    def totalMoney(self, n: int) -> int:
        completeWeeks = n // 7

        # base savings from one complete week is $28...
        bank = completeWeeks * 28

        # ...and every subsequent complete week of savings
        # adds another $7 on top of the weekly savings
        for i in range(completeWeeks):
            bank += 7 * i

        # number of days remaining in final week of savings
        remainingDays = n % 7

        d = {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 7: 28}
        bank += d[remainingDays] + (remainingDays * completeWeeks) 

        return bank
