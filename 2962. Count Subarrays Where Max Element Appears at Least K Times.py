# 4/29/2025 Solutions
class Solution:
    # O(n) time and space complexity
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement = max(nums)
        n = len(nums)

        positions = []
        for i, num in enumerate(nums):
            if num == maxElement:
                positions.append(i)

        ans = 0
        L, R = 0, k - 1
        while R < len(positions):
            if (L == 0):
                distance_to_prev_pos = positions[L]
            else:
                distance_to_prev_pos = positions[L] - positions[L - 1] - 1

            distance_to_end = n - positions[R] - 1

            numSubarrays = (distance_to_prev_pos + 1) * (distance_to_end + 1)
            ans += numSubarrays

            L += 1
            R += 1

        return ans


    # # Naive soln
    # # O(n ^ 2) time
    # # O(1) space
    # def countSubarrays(self, nums: List[int], k: int) -> int:
    #     maxElement = max(nums)
    #     n = len(nums)
    #     ans = 0

    #     for L in range(0, n):
    #         count = 0
            
    #         for R in range(L, n):

    #             if nums[R] == maxElement:
    #                 count += 1

    #             if count >= k:
    #                 ans += 1

    #     return ans


# PREVIOUS SOLUTIONS

# # solution #1: recursion (MLE)
# # O(n) time and O(n^2) space complexity

# from collections import defaultdict
# class Solution:
#     def __init__(self):
#         self.ret = 0
#         self.seen = set()
#         return

#     def countSubarrays(self, nums: List[int], k: int) -> int:
#         # compose frequency table and obtain max int in nums
#         # O(n) time and space complexity
#         freq = defaultdict(int)
#         MAX = 1
#         for num in nums:
#             freq[num] += 1
#             MAX = max(MAX, num)

#         # two pointer recursion
#         # O(n) time and O(n^2) space
#         ret, seen = 0, set()
#         def dp(L, R, count):
#             if (
#                 L == len(nums)
#                 or R < 0
#                 or (L, R) in self.seen 
#                 or count < k
#             ):
#                 return

#             self.ret += 1
#             self.seen.add((L, R))

#             dp(L + 1, R, count - int(nums[L] == MAX))
#             dp(L, R - 1, count - int(nums[R] == MAX))
#             return

#         dp(0, len(nums) - 1, freq[MAX])
#         return self.ret
