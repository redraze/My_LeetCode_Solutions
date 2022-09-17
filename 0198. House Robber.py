class Solution:
    def rob(self, nums: List[int]) -> int:
        # define a separate function that doesn't take a list
        # as an argument (otherwise the result would not be 
        # hashable/cacheable)
        @cache
        def f(i):
            if i >= len(nums):
                return 0
            if i >= len(nums) - 2: 
                return max(nums[i::])
            return max(
                nums[i] + f(i+2),
                nums[i+1] + f(i+3)
            )
        return f(0)
