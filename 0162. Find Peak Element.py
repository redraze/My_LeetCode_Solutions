class Solution:
    # recent solution -- iteration
    def findPeakElement(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L + R) // 2
            if nums[mid] < nums[mid + 1]:
                L = mid + 1
            else:
                R = mid
        return L

    # # previous solution -- recursion
    # def findPeakElement(self, nums: List[int], index=0) -> int:
    #     if len(nums) == 1:
    #         return index
    #     mid = len(nums) // 2
    #     if nums[mid] > nums[mid - 1]:
    #         return index + self.findPeakElement(nums[mid:], mid)
    #     return self.findPeakElement(nums[:mid], index)
