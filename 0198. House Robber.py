# my most recent solution -- using a custom built cache instead of an in-built function wrapper
class Solution:
    def __init__(self) -> None:
        self.cache = {}
        return
    def rob(self, nums: List[int], idx=0) -> int:
        if idx >= len(nums):
            return 0
        if idx not in self.cache:
            self.cache[idx] = max(
                nums[idx] + self.rob(nums, idx + 2),
                self.rob(nums, idx + 1)
            )
        return self.cache[idx]

# # my old solutions
# class Solution:
#     # Solution 2:
#     # iteration.
#     # O(n) runtime and space complexity.
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         if len(nums) == 2:
#             return max(nums[0], nums[1])
#         ans = nums[:]
#         for i in range(2, len(nums)):
#             if i > 2:
#                 ans[i] = max(
#                     nums[i] + ans[i-3],
#                     nums[i] + ans[i-2],
#                     ans[i-1]
#                 )
#                 continue
#             ans[i] = max(
#                 nums[i] + ans[i-2], 
#                 ans[i-1]
#             )
#         return ans[-1]
        
#     '''
#     # Solution 1:
#     # Recursion with memoization.
#     # O(n) runtime and O(n) space complexity.
#     # Uses more space than solution 2 though, since each 
#     # item in 'nums' requires it's own call to 'f()'
#     def rob(self, nums: List[int]) -> int:
#         # define a separate function that doesn't take a list
#         # as an argument (otherwise the result would not be 
#         # hashable/cacheable)
#         @cache
#         def f(i):
#             if i >= len(nums):
#                 return 0
#             if i >= len(nums) - 2: 
#                 return max(nums[i::])
#             return max(
#                 nums[i] + f(i+2),
#                 nums[i+1] + f(i+3)
#             )
#         return f(0)
#     '''
