class Solution:
    def compareWords(self, w1: str, w2: str) -> bool:
        diff = False
        for i in range(self.L):
            if w1[i] != w2[i]:
                if diff:
                    return False
                diff = True
        return True
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        if beginWord in wordList:
            wordList.remove(beginWord)

        ans = 1
        q = deque([beginWord])
        self.L = len(beginWord)
        while q:
            for _ in range(len(q)):
                currentWord = q.popleft()
                if currentWord == endWord:
                    return ans

                for word in list(wordList):
                    if self.compareWords(currentWord, word):
                        wordList.remove(word)
                        q.append(word)

            ans += 1
        
        return 0
