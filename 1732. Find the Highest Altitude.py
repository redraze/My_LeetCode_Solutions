# O(n) time and O(1) space complexity
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = ret = 0
        for num in gain:
            alt += num
            ret = max(ret, alt)
        return ret
