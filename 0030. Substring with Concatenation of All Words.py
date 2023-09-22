class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # solution #1 -- O(kn) runtime (~7000ms lmaoooo)
        # where n = len(s) and k = len(words[i])

        baseDict = {}
        for word in words:
            baseDict[word] = baseDict.get(word, 0) + 1

        used = {}
        L = len(words[0])
        i, j, k = 0, 0, L
        ans = []

        while i <= len(s) - (L * len(words)):
            word = s[j:k]

            if used.get(word, 0) < baseDict.get(word, 0):
                used[word] = used.get(word, 0) + 1
                j += L
                k += L
                
                if used == baseDict:
                    ans.append(i)
                    used = {}
                    i += 1
                    j = i
                    k = i + L

            else:
                used = {}
                i += 1
                j = i
                k = i + L

        return ans  
