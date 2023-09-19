class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        min, switch, k = nums[0], False, 0
        for i in range(0, len(nums)):
            if nums[i] >= min:
                nums[k] = nums[i]
                if switch and nums[k-1] == nums[k]:
                    min = nums[k] + 1
                    switch = False
                else:
                    switch = True
                k += 1
            else:
                switch = False
        return k
