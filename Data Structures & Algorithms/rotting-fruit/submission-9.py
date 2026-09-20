class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        def bfs():
            nonlocal time
            nonlocal fresh   
            while q and fresh > 0:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for row, col in [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]:
                        if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                            grid[row][col] = 2
                            fresh -= 1
                            q.append((row,col))
                time += 1
        bfs()
        if fresh:
            return -1
        else:
            return time