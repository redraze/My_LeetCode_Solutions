class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) time complexity
        # O(m + n) space complexity

        if len(s) != len(t) or set(s) != set(t):
            return False

        sDict, tDict = {}, {}
        for sChar, tChar in zip(s, t):
            sDict[sChar] = sDict.get(sChar, 0) + 1
            tDict[tChar] = tDict.get(tChar, 0) + 1

        if sDict != tDict:
            return False
        return True
