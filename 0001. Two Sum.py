# 9/26/2023 solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict:
                return [i, dict[complement]]
            dict[num] = i
        return

# Previous solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         searched = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in searched:
#                 return [i, searched[complement]]
#             searched[nums[i]] = i
