class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0 or len(grid[0])==0:
            return 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if row>0 and col>0:
                    grid[row][col] += min(grid[row-1][col],grid[row][col-1])
                elif row>0:
                    grid[row][col] += grid[row-1][col]
                elif col>0:
                    grid[row][col] += grid[row][col-1]
        return grid[len(grid)-1][len(grid[0])-1]
