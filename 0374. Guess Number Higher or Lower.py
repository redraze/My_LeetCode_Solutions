# O(log n) time and O(1) space complexity
class Solution:
    def guessNumber(self, n: int) -> int:
        num = int(n/2)
        Min, Max = 0, n

        while True:
            g = guess(num)

            # guess is correct
            if g == 0:
                return num

            # guess is too low
            elif g == 1:
                Min = num
                num = int((Min + Max) / 2) + 1

            # guess is too high
            elif g == -1:
                Max = num
                num = int((Min + Max) / 2)
