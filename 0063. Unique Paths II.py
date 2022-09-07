class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # get grid size
        m = len(obstacleGrid)       # width  (x)
        n = len(obstacleGrid[0])    # height (y)
        
        # label ending position
        grid = {(1,1):1}
        
        # add obstacles to grid
        self.findObstacles(obstacleGrid, grid)
        
        return self.findPaths(grid, m, n)
    
    def findObstacles(self, obstacleGrid, grid):
        for i,row in enumerate(obstacleGrid):
            for j,column in enumerate(row):
                if column == 1:
                    grid[i+1,j+1] = 0
        return
    
    def findPaths(self, grid, m, n):
        index = 2
        while (m,n) not in grid:
            index += 1
            for i in range(1,index):
                j = index-i
                # square outside of grid
                if i>m or j>n:
                    continue
                # square is rock
                if (i,j) in grid:
                    continue
                # square on rightside 
                if i==1:
                    # rock is beneath
                    if grid[i,j-1]==0:
                        grid[i,j] = 0
                    else:
                        grid[i,j] = 1
                    continue
                # square on bottom border 
                if j==1:
                    # rock is adjacent
                    if grid[i-1,j]==0:
                        grid[i,j] = 0
                    else:
                        grid[i,j] = 1
                    continue
                # unique paths is sum of unique paths from 
                # square below and square to the right.
                # if both bordering squares are rocks, 
                # then possible paths from that square is 0.
                # rock propagation!
                grid[i,j] = grid[i-1,j] + grid[i,j-1]
        return grid[m,n]
