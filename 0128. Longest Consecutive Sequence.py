class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n log n) solution
        nums = sorted(nums)
        seen = {}
        ans = 0
        for val in nums:
            if val - 1 in seen:
                seen[val] = seen[val - 1] + 1
            else:
                seen[val] = 1
            ans = max(ans, seen[val])
        print(seen)
        return ans
