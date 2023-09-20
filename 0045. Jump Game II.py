class Solution:
    def jump(self, nums: List[int]) -> int:
        # find the furthest jump possible from range of possible
        # landing spaces after jumping from current location
        def findMaxJumpFromRange(arr: List[int]) -> int:
            maxJump = 0
            for i, val in enumerate(arr):
                maxJump = max(maxJump, i + val)
            return maxJump

        # #   expanded loop
        # jumps, pos = 0, 0
        # L, R = 0, 0
        # while R < len(nums) - 1:
        #     L = R + 1
        #     R = findMaxJumpFromRange(nums[pos:R + 1]) + pos
        #     jumps += 1
        #     pos = L

        #   condensed loop
        jumps, L, R = 0, 0, 0
        while R < len(nums) - 1:
            L, R = R + 1, findMaxJumpFromRange(nums[L:R + 1]) + L
            jumps += 1

        return jumps
