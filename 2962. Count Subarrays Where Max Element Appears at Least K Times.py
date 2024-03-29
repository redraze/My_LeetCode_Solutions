# solution #1: recursion (MLE)
# O(n) time and O(n^2) space complexity

from collections import defaultdict
class Solution:
    def __init__(self):
        self.ret = 0
        self.seen = set()
        return

    def countSubarrays(self, nums: List[int], k: int) -> int:
        # compose frequency table and obtain max int in nums
        # O(n) time and space complexity
        freq = defaultdict(int)
        MAX = 1
        for num in nums:
            freq[num] += 1
            MAX = max(MAX, num)

        # two pointer recursion
        # O(n) time and O(n^2) space
        ret, seen = 0, set()
        def dp(L, R, count):
            if (
                L == len(nums)
                or R < 0
                or (L, R) in self.seen 
                or count < k
            ):
                return

            self.ret += 1
            self.seen.add((L, R))

            dp(L + 1, R, count - int(nums[L] == MAX))
            dp(L, R - 1, count - int(nums[R] == MAX))
            return

        dp(0, len(nums) - 1, freq[MAX])
        return self.ret
