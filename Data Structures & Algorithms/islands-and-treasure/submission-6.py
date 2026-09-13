class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        for r in range (ROWS):
            for c in range (COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        directions = [[1,0], [-1,0], [0,1], [0, -1]]

        while q:

            r,c = q.popleft()
            for dr,dc in directions:
                row = r + dr
                col = c + dc

                if col >= 0 and col < COLS and row >= 0 and row < ROWS and (row,col) not in visit and grid[row][col] == 2147483647:
                    grid[row][col] = 1 + grid[r][c]
                    q.append((row,col))
                    visit.add((row,col))