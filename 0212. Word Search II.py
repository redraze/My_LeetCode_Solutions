class Solution:
    def constructTrie(self, words: List[str]) -> dict:
        trie = {}
        for word in words:
            cur = trie
            for ch in word + '*':
                try:
                    cur = cur[ch]
                except KeyError:
                    cur[ch] = {}
                    cur = cur[ch]
        return trie

    def removeWord(self, trie: dict, word: str) -> None:
        path = []
        cur = trie
        for ch in word:
            path.append(cur)
            cur = cur[ch]
        i = len(word) - 1
        while path:
            cur = path.pop()
            ch = word[i]
            try:
                if cur[ch] == {}:
                    del cur[ch]
                else:
                    break
            except KeyError:
                break
            i -= 1
        return
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.constructTrie(words)
        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        ans = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                
                q = deque([
                    [
                        [i, j],         # current board position
                        root,           # current trie node
                        board[i][j],    # word construction
                        set()           # board positions traversed
                    ]
                ])

                # check character strings built around 
                # board[i][j] via BFS against constructed trie
                while q:
                    [
                        [x, y],
                        trie,
                        word,
                        seenPrev
                    ] = q.popleft()
                    seen = seenPrev.copy()

                    # word in word list found
                    if x == y == -1:
                        if '*' in trie:
                            self.removeWord(root, word)
                            ans.add(word[:len(word) - 1])
                        continue

                    if (x, y) in seen or word[-1] not in trie:
                        continue

                    trie = trie[word[-1]]
                    seen.add((x, y))

                    # check for completed word
                    q.append([
                        [-1, -1],
                        trie,
                        word + '*',
                        seen
                    ])

                    # check surrounding cells
                    # (vertical and horizontal)
                    for v, h in dirs:
                        if (
                            0 <= x + v < m
                            and 0 <= y + h < n
                        ):
                            q.append([
                                [x + v, y + h],
                                trie,
                                word + board[x + v][y + h],
                                seen
                            ])
                            
        return list(ans)
