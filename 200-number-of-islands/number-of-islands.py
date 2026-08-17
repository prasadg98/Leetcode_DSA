class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        num_island = 0

        def dfs(x,y):

            if 0 > x or x >= m or  0 > y or y >= n or grid[x][y] != "1":
                return
            else:
                grid[x][y] = 0 
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x,y+1)
        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_island += 1
                    dfs(i,j)

        return num_island


        




        