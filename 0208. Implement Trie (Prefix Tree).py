class Trie:
    def __init__(self):
        self.root = {}
        return

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word + '*':
            try:
                cur = cur[ch]
            except KeyError:
                cur[ch] = {}
                cur = cur[ch]
        return

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word + '*':
            if ch not in cur:
                return False
            cur = cur[ch]
        return True
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur:
                return False
            cur = cur[ch]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
