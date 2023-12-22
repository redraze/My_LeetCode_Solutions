class Solution:
    # O(n) time and O(1) space complexity
    def maxScore(self, s: str) -> int:
        ones = 0
        for digit in s:
            ones += int(digit)

        score = zeroes = 0
        for digit in s[:-1]:
            if digit == '1':
                ones -= 1
            else:
                zeroes += 1
            score = max(score, zeroes + ones)

        return score
