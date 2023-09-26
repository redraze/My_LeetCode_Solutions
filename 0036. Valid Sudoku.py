class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            s = set()
            for num in row:
                if num == '.':
                    continue
                if num in s:
                    return False
                s.add(num)
        
        # check columns
        for j in range(9):
            s = set()
            for i in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in s:
                    return False
                s.add(num)

        # check sub-boxes
        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                s = set()
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        num = board[x][y]
                        if num == '.':
                            continue
                        if num in s:
                            return False
                        s.add(num)

        return True
