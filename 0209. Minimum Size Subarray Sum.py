# most recent attemp's solution: sliding window -- O(n) time and O(1) space complexity
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j, tally, ans = 0, nums[0], 0
        for i, val in enumerate(nums):
            while tally < target and j < len(nums) - 1:
                j += 1
                tally += nums[j]
            if tally >= target:
                if ans == 0 or j - i + 1 < ans:
                    ans = j - i + 1
            tally -= nums[i]
        return max(ans, 0)

# First solution
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         ans,R = 0,0
#         Sum = 0
#         for L,val in enumerate(nums):
#             while Sum < target:
#                 try:
#                     Sum += nums[R]
#                 except IndexError:
#                     return ans
#                 R += 1
#             if ans == 0 or R - L < ans:
#                 ans = R - L
#             Sum -= val
#         return ans
