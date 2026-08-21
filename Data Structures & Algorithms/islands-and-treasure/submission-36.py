class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        while queue:
            cr, cc, cd = queue.popleft()
            grid[cr][cc] = cd
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] != -1 and (nr, nc) not in visited:
                    queue.append((nr, nc, cd + 1))
                    visited.add((nr, nc))

        
