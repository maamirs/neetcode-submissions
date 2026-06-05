class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        


        rows = len(grid)
        cols = len(grid[0])

        maxarea = 0


        def dfs(r,c):

            if r < 0 or r >= rows:
                return 0
            
            if c < 0 or c >= cols:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            rightsize = dfs(r+1,c)
            leftsize = dfs(r-1, c)
            downsize = dfs(r, c-1)
            upsize = dfs(r , c+1)

            total = rightsize + leftsize + downsize + upsize

            return (total + 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxarea = max(maxarea, dfs(r,c))
        

        return maxarea