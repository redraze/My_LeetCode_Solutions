class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j, val in enumerate(t):
            if i == len(s):
                return True
            if s[i] != val:
                continue
            i += 1
        if i == len(s):
            return True
        return False
