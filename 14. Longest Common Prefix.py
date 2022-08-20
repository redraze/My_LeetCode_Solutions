# my first solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        try:
            for ch in range(len(strs[0])):
                for s in strs[1::]:
                    if strs[0][ch] != s[ch]:
                        return ans
                ans += strs[0][ch]
        except IndexError:
            return ans
        return ans
