# most recent solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        borderIslands = set()
        def flood(x: int, y: int) -> None:
            borderIslands.add((x, y))
            for dx, dy in dirs:
                if (
                    x + dx < 0 or x + dx >= m
                    or y + dy < 0 or y + dy >= n
                    or (x + dx, y + dy) in borderIslands
                ):
                    continue
                if board[x + dx][y + dy] == 'O':
                    flood(x + dx, y + dy)
            return

        # scan top and bottom borders
        for i in range(n):
            if board[0][i] == 'O':
                flood(0, i)
            if board[m - 1][i] == 'O':
                flood(m - 1, i)

        # scan left and right  border:
        for i in range(m):
            if board[i][0] == 'O':
                flood(i, 0)
            if board[i][n - 1] == 'O':
                flood(i, n - 1)

        # iterate through board and flip non-border islands
        for i in range(m):
            for j in range(n):
                if (i, j) not in borderIslands:
                    board[i][j] = 'X'

        return


# PREVIOUS SOLUTION
# # Check each square on border. if land is found on border, DFS that border square.
# # keep land masses that are found from border DFS in memory. iterate through board
# # and flip all land squares not stored in memory
# #
# # Runtime O(n)
# # Space complexity O(n)
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         def DFS(row, column):
#             visited.add((row,column))
#             if board[row][column] == 'O':
#                 borderLands.add((row,column))
#                 # up
#                 if row-1 >= 0 and (row-1,column) not in visited:
#                     DFS(row-1,column)
#                 # down
#                 if row+1 < r and (row+1,column) not in visited:
#                     DFS(row+1,column)
#                 # left
#                 if column-1 >= 0 and (row,column-1) not in visited:
#                     DFS(row,column-1)
#                 # right
#                 if column+1 < c and (row,column+1) not in visited:
#                     DFS(row,column+1)
#             return
#         r = len(board)
#         c = len(board[0])
#         visited = set()
#         borderLands = set()
#         # top border
#         for i in range(1,c):
#             if (0,i) not in visited:
#                 DFS(0,i)
#         # right border
#         for i in range(1,r):
#             if (i,c-1) not in visited:
#                 DFS(i,c-1)
#         # bottom border
#         for i in range(c-1):
#             if (r-1,i) not in visited:
#                 DFS(r-1,i)
#         # left border
#         for i in range(r):
#             if (i,0) not in visited:
#                 DFS(i,0)
#         # flip non-border land formations
#         for i,j in itertools.product(range(r),range(c)):
#             if board[i][j] == 'O' and (i,j) not in borderLands:
#                 board[i][j] = 'X'
#         return
