class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visit = set()

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        while q:
            r,c = q.popleft()
            for row,col in [(r,c-1),(r,c+1),(r-1,c),(r+1,c)]:
                if row >= 0 and row < ROWS and col >= 0 and col < COLS and grid[row][col] == 2147483647 and (row,col) not in visit:
                    grid[row][col] = 1 + grid[r][c]
                    visit.add((row,col))
                    q.append((row,col))