class Solution:
    def __init__(self) -> None:
        self.cache = {}
        return
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        if s not in self.cache:
            self.cache[s] = any(self.wordBreak(s[len(word):], wordDict) if word == s[:len(word)] else False for word in wordDict)
        return self.cache[s]
