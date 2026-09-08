class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        res = []

        def dfs(r,c, oceanSet, curHeight):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r][c] < curHeight or (r,c) in oceanSet :
                return
                
            oceanSet.add((r,c))
            dfs(r-1,c, oceanSet, heights[r][c])
            dfs(r+1 ,c, oceanSet, heights[r][c])
            dfs(r,c-1, oceanSet, heights[r][c])
            dfs(r,c+1, oceanSet, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])

        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])


        for (r,c) in pacific:
            dfs(r,c, pacific, heights[r][c])
        
        for (r,c) in atlantic:
            dfs(r,c, atlantic, heights[r][c])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append([r,c])

        return res

        
