class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            nonlocal islands
            if r >= 0 and r < ROW and c >= 0 and c < COL:
                if grid[r][c] == "0":
                    return 
                else:
                    grid[r][c] = "0"
                    dfs(r-1,c)
                    dfs(r+1,c)
                    dfs(r,c-1)
                    dfs(r,c+1)
                    return
                    

            
                islands += 1
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands
            

