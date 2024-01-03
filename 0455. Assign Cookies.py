class Solution:
    # O(n log n) time and O(1) space complexity
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g, s = sorted(g), sorted(s)
        i = j = 0

        try:
            while i < len(g):
                while s[j] < g[i]:
                    j += 1
                i += 1
                j += 1
        except IndexError:
            pass

        return i
