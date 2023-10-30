class Solution:
    # my most recent solution -- iteration
    # O(log n) time and O(1) space complexity
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L + R) // 2

            # array is in order -> min is in left side of array
            if nums[L] < nums[R]:
                R = mid - 1
                continue
            
            # left side of array is in order -> min is in right side of array
            if nums[mid] >= nums[L]:
                L = mid + 1

            # right side of array is in order -> min is in left side of array
            else:
                R = mid

        return nums[L]

    # # my previous solution -- recursion
    # def findMin(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     L, R = nums[0], nums[-1]
    #     # nums is not rotated
    #     if L < R:
    #         return nums[0]
    #     m = len(nums)//2
    #     if nums[m] > L:
    #         # loop on right
    #         return self.findMin(nums[m+1::])
    #     # loop on left
    #     return self.findMin(nums[1:m+1])
