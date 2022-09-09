class Solution:
    # Solution 1
    # runtime O(n) with k operations, where 
    # k = number of non-zero elements in array
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = (0, 1)
        while j < len(nums):
            try:
                if nums[i] == 0:
                    while j < len(nums) and nums[j] == 0:
                        j += 1
                    nums[i] = nums[j]
                    nums[j] = 0
                i += 1
                j += 1
            except IndexError:
                return
        return
