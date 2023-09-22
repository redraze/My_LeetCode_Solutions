class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # solution #1: brute force
        # O(kn) runtime, where n = len(s) and k = len(words[i])
        def removeWord(s: str, d: dict) -> dict:
            if d[s] == 1:
                del d[s]
            else:
                d[s] -= 1
            return d
        def addWord(s: str, d: dict) -> dict:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
            return d
        def resetDict(d: dict) -> dict:
            for word in words:
                addWord(word, d)
            return d

        used, unUsed = {}, resetDict({})
        L = len(words[0])
        i, j, k = 0, 0, L
        ans = []

        while i <= len(s) - (L * len(words)):
            word = s[j:k]

            if word in unUsed:
                removeWord(word, unUsed)
                addWord(word, used)
                j += L
                k += L

                # all words have been used!
                if unUsed == {}:
                    ans.append(i)
                    used, unUsed = {}, resetDict({})
                    i += 1
                    j = i
                    k = i + L

            else:
                used, unUsed = {}, resetDict({})
                i += 1
                j = i
                k = i + L

        return ans  
