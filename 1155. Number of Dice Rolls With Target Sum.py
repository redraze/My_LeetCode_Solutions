class Solution:
    # O(n * k * target) time and space complexity
    def __init__(self) -> None:
        self.memo = {}
        self.mod = 10**9 + 7
        return
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == target == 0:
            return 1
        elif n == 0:
            return 0

        if (n, k, target) in self.memo:
            return self.memo[(n, k, target)]

        self.memo[(n, k, target)] = sum(
            self.numRollsToTarget(
                n - 1,
                k,
                i
            ) for i in range(
                max(
                    0,
                    target - k
                ),
                target
            )
        )

        return self.memo[(n, k, target)] % self.mod
