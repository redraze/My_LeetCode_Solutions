class Solution:
    def findPeakElement(self, nums: List[int], index=0) -> int:
        if len(nums) == 1:
            return index
        m = len(nums)//2
        if nums[m] > nums[m-1]:
            return index + self.findPeakElement(nums[m::], m)
        return self.findPeakElement(nums[0:m], index)
