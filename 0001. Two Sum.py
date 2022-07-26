###
#
# tried a brute force saultion at first, but eventually peeked at the solution. ended up learning a lot about hash tables!
#
###


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        searched = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in searched:
                return [i, searched[complement]]
            searched[nums[i]] = i
