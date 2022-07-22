###
#
# I actually solved this problem really quickly, and afterwards decided to jump to problem #42, Trapping Rain Water
#
###


class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        A = 0
        while L != R:
            if min(height[L], height[R]) * (R - L) > A:
                A = min(height[L], height[R]) * (R - L)
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
        return A
