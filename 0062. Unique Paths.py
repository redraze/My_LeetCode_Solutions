# the number of possible paths in each sqaure is equal to the 
# sum of the number possible paths in the square to its right
# (zero if on the rightside border) and the number of possible 
# paths in the square directly under it (or zero if on the bottom)

# runtime: O(m x n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = {(1,1):1}
        index = 3
        while (m,n) not in grid:
            for i in range(1, index):
                if i>m or index-i>n:
                    continue
                if i == 1 or index-i == 1:
                    grid[i,index-i] = 1
                    continue
                grid[i,index-i] = grid[i-1,index-i] + grid[i,index-i-1]
            index += 1
        return grid[m,n]
