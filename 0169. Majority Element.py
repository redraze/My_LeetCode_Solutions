#  Fancy Shamncy Moore Voting algo: O(n) time and O(0) space complexity
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, count = 0, 0
        for val in nums:
            if count == 0:
                ans = val
              
            if val == ans:
                count += 1
            else:
                count -= 1

        return ans


# #  Hashmap solution: O(n) time/space complexity
# #  (My intuitive solution) 
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:

#         d = {}
#         for val in nums:
#             try:
#                 d[val] += 1
#             except KeyError:
#                 d[val] = 1

#         ans = nums[0]
#         for key in d:
#             if d[key] > d[ans]:
#                 ans = key

#         return ans
