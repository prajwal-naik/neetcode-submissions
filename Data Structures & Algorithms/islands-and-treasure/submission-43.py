class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append([i, j, 0])

        while queue:
            r, c, curDis = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = curDis + 1
                    queue.append((nr, nc, curDis + 1))

        

