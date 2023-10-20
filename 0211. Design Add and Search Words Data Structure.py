class WordDictionary:

    def __init__(self):
        self.root = {}
        return

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word + '*':
            try:
                cur = cur[ch]
            except KeyError:
                cur[ch] = {}
                cur = cur[ch]
        return

    def search(self, word: str, cur=None) -> bool:
        if not cur:
            cur = self.root
            word += '*'
        for i, ch in enumerate(word):
            if ch == '.':
                for key in cur.keys():
                    if self.search(word[i + 1::], cur[key]):
                        return True
            try:
                cur = cur[ch]
            except KeyError:
                return False
        return True


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
