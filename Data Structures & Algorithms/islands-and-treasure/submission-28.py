class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(r, c):
            treasures = []
            queue = deque()
            visited  = set()
            queue.append((r, c, 0))
            visited.add((r, c))
            while queue:
                cr, cc, curLen = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visited and grid[nr][nc] != -1:
                        if grid[nr][nc] == 0:
                            treasures.append(curLen + 1)
                        else:
                            visited.add((nr, nc))
                            queue.append((nr, nc, curLen + 1))

            return treasures

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2147483647:
                    curTreasures = bfs(i, j)
                    print(curTreasures)
                    grid[i][j] = min(curTreasures)
        