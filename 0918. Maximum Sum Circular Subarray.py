class Solution:
    # solution 2 -- Kadane's algo
    # O(n) time and O(1) space complexity
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_num = max_sum = max_tally = min_sum = min_tally = nums[0]

        for val in nums[1:]:
            max_num = max(max_num, val)

            max_tally = max(max_tally + val, val)
            max_sum = max(max_sum, max_tally)

            min_tally = min(min_tally + val, val)
            min_sum = min(min_sum, min_tally)

        if max_num <= 0:
            return max_num
        return max(max_sum, sum(nums) - min_sum)


    # # solution 1 -- TLE
    # # O(n^2) time and O(1) space complexity
    # def maxSubarraySumCircular(self, nums: List[int]) -> int:
    #     ans = nums[0]
    #     n = len(nums)
    #     for i in range(n):
    #         idx = i
    #         tally = nums[idx]
    #         for _ in range(n - 1):
    #             idx += 1
    #             if idx == n:
    #                 idx = 0
    #             val = nums[idx]
    #             tally = max(tally + val, val)
    #             ans = max(ans, tally)
    #     return ans
