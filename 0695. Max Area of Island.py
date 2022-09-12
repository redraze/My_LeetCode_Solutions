import itertools

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def visitIsland(i, j):
            if (
                (i,j) not in visited
                and i < R and i >= 0
                and j < C and j >= 0
                and grid[i][j] != 0

            ):
                visited.add((i,j))
                directions = [
                    [i+1,j],
                    [i-1,j],
                    [i,j+1],
                    [i,j-1]
                ]
                area = 1
                for d in directions:
                    area += visitIsland(d[0], d[1])
                return area
            visited.add((i,j))
            return 0
        
        visited = set()
        R,C = len(grid), len(grid[0])
        ans = 0
        for i,j in itertools.product(range(R),range(C)):
            if grid[i][j] == 1 and (i,j) not in visited:
                area = visitIsland(i, j)
                if area > ans:
                    ans = area
                continue
            visited.add((i,j))
        return ans
