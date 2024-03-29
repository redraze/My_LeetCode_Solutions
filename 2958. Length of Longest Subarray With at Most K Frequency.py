# O(n) time and space complexity
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        L, ret = 0, 0

        for (R, num) in enumerate(nums):
            freq[num] += 1

            while freq[num] > k:
                freq[nums[L]] -= 1
                L += 1

            ret = max(ret, R - L + 1)

        return ret
