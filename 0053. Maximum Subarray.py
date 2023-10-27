class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, tally = -(10**4), 0
        for val in nums:
            tally += val
            ans = max(ans, tally)
            if tally < 0:
                tally = 0
        return ans
