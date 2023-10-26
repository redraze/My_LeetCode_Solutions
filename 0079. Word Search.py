class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # check to make sure all letters in word are present in board
        letters = set(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] in letters:
                    letters.remove(board[i][j])
        if letters:
            return False
        del letters

        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        def search(x: int, y: int, seen: set, idx=0) -> bool:
            if (
                x >= m or x < 0
                or y >= n or y < 0
                or (x, y) in seen
                or board[x][y] != word[idx]
            ):
                return False

            if idx == len(word) - 1:
                return True

            seen.add((x, y))
            
            for i, j in dirs:
                if search(
                    x + i, y + j,
                    seen,
                    idx + 1
                ):
                    return True
            
            seen.remove((x, y))

            return False

        for i in range(m):
            for j in range(n):
                if search(i, j, set()):
                    return True

        return False
