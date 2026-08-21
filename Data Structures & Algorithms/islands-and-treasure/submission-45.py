class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque([])
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        while queue:
            r, c, curDis = queue.popleft()
            grid[r][c] = curDis
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visited and grid[nr][nc] != -1:
                    visited.add((nr, nc))
                    queue.append((nr, nc, curDis + 1))

        

