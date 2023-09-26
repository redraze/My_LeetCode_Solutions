class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = {}
        for ch in t:
            tDict[ch] = tDict.get(ch, 0) + 1

        L = R = 0
        used, overUsed = {}, {}
        ans = ""

        while R < len(s):
            # increment R until slice contains all letters in t
            if s[R] in tDict:
                if used.get(s[R], 0) < tDict[s[R]]:
                    used[s[R]] = used.get(s[R], 0) + 1
                else:
                    overUsed[s[R]] = overUsed.get(s[R], 0) + 1 
            R += 1

            # increment L until slice doesn't contain all letters in t
            while used == tDict:
                if s[L] in tDict:
                    #  update answer
                    if ans == "":
                        ans = s[L:R]
                    elif len(s[L:R]) < len(ans):
                        ans = s[L:R]

                    if overUsed.get(s[L], 0) != 0:
                        overUsed[s[L]] -= 1
                    else:
                        used[s[L]] -= 1
                L += 1

            # trim extra letters from left-hand side of slice
            while L < len(s) and s[L] not in tDict:
                L += 1

        return ans
