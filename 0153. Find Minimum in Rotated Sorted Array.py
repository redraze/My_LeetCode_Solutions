class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        L, R = nums[0], nums[-1]
        # nums is not rotated
        if L < R:
            return nums[0]
        m = len(nums)//2
        if nums[m] > L:
            # loop on right
            return self.findMin(nums[m+1::])
        # loop on left
        return self.findMin(nums[1:m+1])
