class Solution:
    # solution 2: grid reduction
    # O(m * n) time and O(1) space complexity,
    # where m is num rows and n is num columns
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # iterate along left-hand column
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # iterate along top row
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]

        # iterate through the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(
                    grid[i - 1][j],
                    grid[i][j - 1]
                )

        return grid[-1][-1]


    # # solution 1: flood fill with a queue
    # # O(m * n) time and space complexity,
    # # where m is num rows and n is num columns
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     q = deque([(0, 0)])
    #     seen = {(0, 0)}

    #     while q:
    #         x, y = q.popleft()

    #         # both up and left cells are within grid
    #         if x - 1 >= 0 and y - 1 >= 0:
    #             grid[x][y] = grid[x][y] + min(
    #                 grid[x - 1][y],
    #                 grid[x][y - 1]
    #             )
    #         # only left cell is within grid
    #         elif x - 1 >= 0:
    #             grid[x][y] = grid[x][y] + grid[x - 1][y]
    #         # only up cell is within grid
    #         elif y - 1 >= 0:
    #             grid[x][y] = grid[x][y] + grid[x][y - 1]

    #         # lower cell is within grid
    #         if x + 1 < m and (x + 1, y) not in seen:
    #             q.append((x + 1, y))
    #             seen.add((x + 1, y))
    #         # right cell is within grid
    #         if y + 1 < n and (x, y + 1) not in seen:
    #             q.append((x, y + 1))
    #             seen.add((x, y + 1))

    #     return grid[x][y]
