class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        while queue:
            curX, curY, curDis = queue.popleft()
            for dr, dc in directions:
                nr, nc = curX + dr, curY + dc
                if nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visited and grid[nr][nc] != -1:
                    grid[nr][nc] = curDis + 1
                    queue.append((nr, nc, curDis + 1))
                    visited.add((nr, nc))
