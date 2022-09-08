# iteratively searches nums excluding half of nums based on
# if the target is bigger or smaller than the center item in nums
# runtime O(log n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target > nums[-1] or target < nums[0]:
            return -1
        left = 0
        right = len(nums) - 1
        while True:
            index = left + int((right - left)/2)
            for i in [left, right, index]:
                try:
                    if target == nums[i]:
                        return i
                except IndexError:
                    print(i)
                    return
            if left == right:
                break
            if target > nums[index] and target != nums[left]:
                left = index + 1
                continue
            right = index
        return -1
