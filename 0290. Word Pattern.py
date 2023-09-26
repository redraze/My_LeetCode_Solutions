class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # attempt #1 -- O(n) time and space complexity
        words = s.split(' ')
        if (
            len(words) != len(pattern)
            or len(set(pattern)) != len(set(words))
        ):
            return False

        d = {}
        for ch, word in zip(pattern, words):
            if (ch in d and d[ch] != word):
                return False
            d[ch] = word
        return True
