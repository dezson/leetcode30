class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        helper = [[True] * (len(grid[x])) for x in range(len(grid))]

        def dfs(grid, x, y, h):
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1:
                return False
            if h[x][y] == False:
                return False
            else:
                h[x][y] = False
                if grid[x][y] == "1":
                    dfs(grid,x+1,y,h)
                    dfs(grid,x-1,y,h)
                    dfs(grid,x,y+1,h)
                    dfs(grid,x,y-1,h)
                    return True
                return False

        for i in range(len(grid)):
            for k in range(len(grid[i])):
                if dfs(grid,i,k,helper):
                    cnt+=1
        return cnt
