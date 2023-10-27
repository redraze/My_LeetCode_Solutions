class Solution:
    # most recent solution -- iteration
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0

        L, R = 0, len(nums)
        while L < R:
            mid = (L + R) // 2
            if target > nums[mid]:
                L = mid + 1 
            else:
                R = mid
        return L

    # # previous solution -- recursion
    # def searchInsert(self, nums: List[int], target: int, left=0) -> int:
    #     if target > nums[-1]:
    #         return len(nums)
    #     if target == nums[-1]:
    #         return len(nums) - 1
    #     if target < nums[0] or target == nums[0]:
    #         return 0
        
    #     right = len(nums) - 1
    #     index = left + int((right-left)/2)
    #     if target > nums[index]:
    #         return self.searchInsert(nums, target, index+1)
    #     return self.searchInsert(nums[0:index], target, left)
