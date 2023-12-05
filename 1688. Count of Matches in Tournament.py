class Solution:
    # O(1) time and space complexity
    def numberOfMatches(self, n: int) -> int:
        return n - 1

    # # O(log n) time and O(1) space complexity
    # def numberOfMatches(self, n: int) -> int:
    #     matches = 0

    #     while n > 1:
    #         matches += n // 2
    #         n -= n // 2

    #     return matches
