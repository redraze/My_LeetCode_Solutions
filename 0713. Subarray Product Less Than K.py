class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        L,ans = 0,0
        prod = 1
        for R,val in enumerate(nums):
            if val < k:
                ans += 1
            prod *= val
            while prod >= k and L < len(nums)-1:
                prod /= nums[L]
                L += 1
            if R - L > 0:
                ans += R - L
        return ans
