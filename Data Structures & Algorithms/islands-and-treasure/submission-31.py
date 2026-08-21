class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    # visited.add((i, j))
                    queue.append((i, j, 0))
        while queue:
            cr, cc, curDis = queue.popleft()
            visited.add((cr, cc))
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if nr in range(ROWS) and nc in range(COLS) and (grid[nr][nc] != -1) and (nr, nc) not in visited:
                    grid[nr][nc] = min(grid[nr][nc], curDis + 1)
                    visited.add((nr, nc))
                    queue.append((nr, nc, curDis + 1))
            
        

