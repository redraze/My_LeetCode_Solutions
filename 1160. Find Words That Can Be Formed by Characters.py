class Solution:
    # O(m + nl) time and O(m) space complexity
    # where m is len(chars), n is len(words), 
    # and l is average length of each word in words
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsDict = defaultdict(int)
        for ch in chars:
            charsDict[ch] += 1

        ans = 0
        for word in words:
            preDict = charsDict.copy()
            check = True

            for ch in word:
                if ch not in preDict:
                    check = False
                    break

                if preDict[ch] == 1:
                    del preDict[ch]
                else:
                    preDict[ch] -= 1

            if check:
                ans += len(word)

        return ans
