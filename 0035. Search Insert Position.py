class Solution:
    def searchInsert(self, nums: List[int], target: int, left=0) -> int:
        # end conditions
        if target > nums[-1]:
            return len(nums)
        if target == nums[-1]:
            return len(nums) - 1
        if target < nums[0] or target == nums[0]:
            return 0
        
        # recurse conditions
        right = len(nums) - 1
        index = left + int((right-left)/2)
        if target > nums[index]:
            return self.searchInsert(nums, target, index+1)
        return self.searchInsert(nums[0:index], target, left)
