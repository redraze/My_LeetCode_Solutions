class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #   Solution #2: 2-pointer fliperoo!
        def flip(arr: List[int], L: int, R: int) -> None:
            while L < R:
                temp = arr[R]
                arr[R] = arr[L]
                arr[L] = temp
                L += 1
                R -= 1
            return
        
        K = k % len(nums)
        flip(nums, 0, len(nums) - 1)
        flip(nums, 0, K - 1)
        flip(nums, K, len(nums) - 1)
        return

        # #   Solution #1: slicing
        # K = k % len(nums)
        # copy = nums[len(nums) - K::] + nums[0:len(nums) - K]
        # for i, val in enumerate(copy):
        #     nums[i] = val
        # return
