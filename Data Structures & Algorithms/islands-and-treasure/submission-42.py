class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append([i, j, 0])
                    visited.add((i, j))

        while queue:
            r, c, curDis = queue.popleft()
            grid[r][c] = curDis
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 2147483647 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, curDis + 1))

        

