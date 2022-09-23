class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans,R = 0,0
        Sum = 0
        for L,val in enumerate(nums):
            while Sum < target:
                try:
                    Sum += nums[R]
                except IndexError:
                    return ans
                R += 1
            if ans == 0 or R - L < ans:
                ans = R - L
            Sum -= val
        return ans
