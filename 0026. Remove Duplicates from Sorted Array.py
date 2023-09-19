class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        min, k = nums[0], 0
        for i in range(0, len(nums)):
            if nums[i] >= min:
                nums[k] = nums[i]
                k += 1
                min = nums[i] + 1
        return k
