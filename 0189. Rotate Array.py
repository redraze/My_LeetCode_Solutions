class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Method 2: using slicing. runtime O(k)
        # eliminate some edge cases:
        # no rotations, nums length of 1, and 
        # completely rotating through the entire length of nums
        if k == 0 or len(nums) == 1 or k == len(nums):
            return
        k = k % len(nums)
        # nums[:] not nums.
        # using only nums will instantiate a copy of nums.
        # using nums[:] ensures changing the input nums,
        # which is what this problem requires.
        nums[:] = nums[-k::] + nums[0:len(nums)-k]
        return 
        
        """
        # Method 1: using python's build it methods. Runtime O(n^k)
        while k > 0:
            nums.insert(0,nums[-1])
            nums.pop(-1)
            k -= 1
        return
        """
