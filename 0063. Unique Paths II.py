class Solution:
    # most recent solution 2: in-place tabulation
    # # O(m * n) time and O(1) space complexity,
    # # where m is num rows and n is num columns    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # I'm going to keep track of how many unique paths there are
        # using negative int's since rock is using positive int and
        # I don't want to spend extra resources iterating though to flip
        # rock's int sign. will this save space? do negative int's take up
        # so much more space that this approach becomes not so good???
        obstacleGrid[0][0] = -1
        
        # iterate left-hand column
        for i in range(1, m):
            # rock!
            if obstacleGrid[i][0] == 1:
                break
            obstacleGrid[i][0] = -1

        # iterate top row
        for i in range(1, n):
            # rock!
            if obstacleGrid[0][i] == 1:
                break
            obstacleGrid[0][i] = -1


        for i in range(1, m):
            for j in range(1, n):
                # rock!
                if obstacleGrid[i][j] == 1:
                    continue
                if obstacleGrid[i - 1][j] != 1:
                    obstacleGrid[i][j] += obstacleGrid[i - 1][j]
                if obstacleGrid[i][j - 1] != 1:
                    obstacleGrid[i][j] += obstacleGrid[i][j - 1]

        return obstacleGrid[-1][-1] * -1

    # # most recent solution 1: DFS/BFS -- TLE
    # # O(?) time and space complexity
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
    #         return 0

    #     # replace stack with deque([(0,0)]) and use popleft() for BFS
    #     stack = [(0,0)]
    #     ans = 0
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])

    #     while stack:
    #         x, y = stack.pop()

    #         # grid cell is out of bounds, or rock
    #         if x == m or y == n or obstacleGrid[x][y] == 1:
    #             continue
            
    #         # end cell reached via unique pathway
    #         elif x == m - 1 and y == n - 1:
    #             ans += 1
    #             continue

    #         stack.append((x + 1, y))
    #         stack.append((x, y + 1))

    #     return ans

    
    # # previous solution
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     # get grid size
    #     m = len(obstacleGrid)       # width  (x)
    #     n = len(obstacleGrid[0])    # height (y)
        
    #     # label ending position
    #     grid = {(1,1):1}
        
    #     # add obstacles to grid
    #     self.findObstacles(obstacleGrid, grid)
        
    #     return self.findPaths(grid, m, n)
    
    # def findObstacles(self, obstacleGrid, grid):
    #     for i,row in enumerate(obstacleGrid):
    #         for j,column in enumerate(row):
    #             if column == 1:
    #                 grid[i+1,j+1] = 0
    #     return
    
    # def findPaths(self, grid, m, n):
    #     index = 2
    #     while (m,n) not in grid:
    #         index += 1
    #         for i in range(1,index):
    #             j = index-i
    #             # square outside of grid
    #             if i>m or j>n:
    #                 continue
    #             # square is rock
    #             if (i,j) in grid:
    #                 continue
    #             # square on rightside 
    #             if i==1:
    #                 # rock is beneath
    #                 if grid[i,j-1]==0:
    #                     grid[i,j] = 0
    #                 else:
    #                     grid[i,j] = 1
    #                 continue
    #             # square on bottom border 
    #             if j==1:
    #                 # rock is adjacent
    #                 if grid[i-1,j]==0:
    #                     grid[i,j] = 0
    #                 else:
    #                     grid[i,j] = 1
    #                 continue
    #             # unique paths is sum of unique paths from 
    #             # square below and square to the right.
    #             # if both bordering squares are rocks, 
    #             # then possible paths from that square is 0.
    #             # rock propagation!
    #             grid[i,j] = grid[i-1,j] + grid[i,j-1]
    #     return grid[m,n]
