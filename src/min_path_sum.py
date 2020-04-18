class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for x in range(1,len(grid)):
            grid[x][0] = grid[x-1][0] + grid[x][0]

        for y in range(1,len(grid[0])):
            grid[0][y] = grid[0][y] + grid[0][y-1]

        for m in range(1,len(grid)):
            for j in range(1, len(grid[0])):
                grid[m][j] += min(grid[m-1][j], grid[m][j-1])

        return grid[len(grid)-1][len(grid[0])-1]
