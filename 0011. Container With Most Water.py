class Solution:
    def maxArea(self, height: List[int]) -> int:
        # solution #2 -- O(n) time complexity
        L, R, ans = 0, len(height) - 1, 0
        while L < R:
            current = (R - L) * min(height[R], height[L])
            ans = max(ans, current)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return ans

        # # solution #1 -- O(n^2) time complexity
        # i = 0
        # ans = 0
        # while i < len(height):
        #     for j in range(i + 1, len(height)):
        #         current = (j - i) * min(height[i], height[j])
        #         ans = max(current, ans)
        #     i += 1
        # return ans
