class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthestJump = 0
        for i, val in enumerate(nums):
            if i > furthestJump:
                return False
            furthestJumpFromCurrentIndex = i + val
            if furthestJumpFromCurrentIndex > furthestJump:
                furthestJump = furthestJumpFromCurrentIndex
        return True


        # # Initial solution: dp
        # if len(nums) <= 1:
        #     return True
        # if nums[0] == 0:
        #     return False
        # for i in range(nums[0], 0, -1):
        #     if self.canJump(nums[i::]):
        #         return True
        # return False
