class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        dirs = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]
        def flood(x, y):
            grid[x][y] = '0'
            for dx, dy in dirs:
                if (
                    x + dx < 0 or x + dx >= m
                    or y + dy < 0 or y + dy >= n
                ):
                    continue
                if int(grid[x + dx][y + dy]):
                    flood(x + dx, y + dy)
            return

        for i in range(m):
            for j in range(n):
                if int(grid[i][j]):
                    flood(i, j)
                    ans += 1
        return ans

# # old solution
# import itertools
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # memoize grid squares that have been visited,
#         # and prevent input mutation
#         scanned = set()
#         islands = 0
#         R,C = len(grid), len(grid[0])
#         # without itertools -- a list comprehension expression
#         # for p in [(i,j) for i in range(R) for j in range(C)]:
#         #    i,j = p[0],p[1]
#         #    ...
#         for i,j in itertools.product(range(R),range(C)):
#             if (
#                 grid[i][j] == '1'
#                 and (i,j) not in scanned
#             ):
#                 islands += 1
#                 scanned.add(
#                     (i,j)
#                 )
#                 scanned = self.scanIsland(grid, scanned, i, j, R, C)
#         return islands
    
#     # add each square from each island to 
#     # visited set via flood fill algorithm
#     def scanIsland(self, grid, scanned, i ,j, R, C):
#         directions = [
#             [i-1,j],
#             [i+1,j],
#             [i,j-1],
#             [i,j+1]
#         ]
#         for d in directions:
#             if (
#                 d[0] < R and d[0] >= 0
#                 and d[1] < C and d[1] >= 0
#                 and (d[0],d[1]) not in scanned
#                 and grid[d[0]][d[1]] == '1'
#             ):
#                 scanned.add(
#                     (d[0], d[1])
#                 )
#                 scanned = self.scanIsland(grid, scanned, d[0],d[1], R, C)
#         return scanned
