class Solution:
    # O(n) time and O(1) space complexity
    def largestGoodInteger(self, num: str) -> str:
        ret = cur = ""

        for digit in num:
            if not cur:
                cur += digit
                continue

            if cur[-1] == digit:
                cur += digit
            else:
                cur = digit
                continue

            if len(cur) == 3:
                if cur > ret:
                    ret, cur = cur, ""
                else:
                    cur = ""
                
        return ret
