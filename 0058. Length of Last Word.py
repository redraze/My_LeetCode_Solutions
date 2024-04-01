class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # # O(n) time and O(1) space complexity
        # return len(s.strip().split(' ')[-1])

        # optimized -- still O(n) time and O(1) space complexity
        i = len(s) - 1
        ret = 0
        while i >= 0:
            if s[i] == ' ':
                if ret > 0:
                    return ret
                i -= 1
                continue

            ret += 1
            i -= 1

        return ret
