class Solution:
    def reverseString(self, s: List[str]) -> None:
        L, R = (0, len(s)-1)
        while L != R and L < R:
            s[L], s[R] = (s[R], s[L])
            L += 1
            R -= 1
        return s
