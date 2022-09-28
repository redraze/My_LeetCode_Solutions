# Check each square on border. if land is found on border, DFS that border square.
# keep land masses that are found from border DFS in memory. iterate through board
# and flip all land squares not stored in memory
#
# Runtime O(n)
# Space complexity O(n)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def DFS(row, column):
            visited.add((row,column))
            if board[row][column] == 'O':
                borderLands.add((row,column))
                # up
                if row-1 >= 0 and (row-1,column) not in visited:
                    DFS(row-1,column)
                # down
                if row+1 < r and (row+1,column) not in visited:
                    DFS(row+1,column)
                # left
                if column-1 >= 0 and (row,column-1) not in visited:
                    DFS(row,column-1)
                # right
                if column+1 < c and (row,column+1) not in visited:
                    DFS(row,column+1)
            return
        r = len(board)
        c = len(board[0])
        visited = set()
        borderLands = set()
        # top border
        for i in range(1,c):
            if (0,i) not in visited:
                DFS(0,i)
        # right border
        for i in range(1,r):
            if (i,c-1) not in visited:
                DFS(i,c-1)
        # bottom border
        for i in range(c-1):
            if (r-1,i) not in visited:
                DFS(r-1,i)
        # left border
        for i in range(r):
            if (i,0) not in visited:
                DFS(i,0)
        # flip non-border land formations
        for i,j in itertools.product(range(r),range(c)):
            if board[i][j] == 'O' and (i,j) not in borderLands:
                board[i][j] = 'X'
        return
