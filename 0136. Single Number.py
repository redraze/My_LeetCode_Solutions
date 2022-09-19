class Solution:
	# runtime O(n)
	# space complexity O(1)
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
		# XOR n with each number in 'nums'.
		# since any integer XOR'd with itself is zero,
		# 'ans' will end up being the only number in
		# 'nums' that only occurs once
        for n in nums:
			ans ^= n
        return ans
