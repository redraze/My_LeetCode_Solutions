'''

My first thought was to reuse the two pointer method from the previous problem, 3Sum.
which works, except the run time exceeds LeetCode's time limit. 

could there be a better way?

'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = self.sortList(nums)
        return self.findClosest(nums, target)

    def sortList(self, nums: List[int]) -> List[int]:
        # TODO write own sorting algo
        # python sorted() runtime O(n logn)
        return sorted(nums)
    
    # two pointer method; runtime O(n^2)
    def findClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        for j in range(1, len(nums)):
            i = j - 1
            k = j + 1
            while i >= 0 and k < len(nums):
                Sum = nums[i] + nums[j] + nums[k]
                try:
                    if abs(target - Sum) < abs(target - ans):
                        ans = Sum
                except NameError:
                    ans = Sum
                if Sum > target:
                    i -= 1
                elif Sum < target:
                    k += 1
                else:   # Sum == target
                    return Sum
        return ans
