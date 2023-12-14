class Solution:
    # solution 2: in-place grid modification with a trick!
    # O(m * n) time and O(m + n) space complexity
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        r, c = [0] * m, [0] * n

        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                r[i] += num
                c[j] += num

        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * (r[i] + c[j]) - (m + n)

        return grid

    # # solution 1
    # # O(m * n) time and space complexity
    # def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
    #     r = {
    #         0: [0] * len(grid),
    #         1: [0] * len(grid)
    #     }
    #     c = {
    #         0: [0] * len(grid[0]),
    #         1: [0] * len(grid[0])
    #     }

    #     for i, row in enumerate(grid):
    #         for j, num in enumerate(row):
    #             r[num][i] += 1
    #             c[num][j] += 1

    #     diff = []
    #     for i in range(len(grid)):
    #         diff.append([])
    #         for j in range(len(grid[0])):
    #             zeroes = r[0][i] + c[0][j]
    #             ones = r[1][i] + c[1][j]
    #             diff[i].append(ones - zeroes)

    #     return diff
