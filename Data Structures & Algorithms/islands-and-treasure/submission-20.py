class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def bfs(i, j):
            visited = set()
            queue = deque()
            queue.append((i, j, 0))
            treasures = []
            while queue:
                
                r, c, curLen = queue.popleft()
                visited.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(ROWS) and nc in range(COLS):
                        if grid[nr][nc] == 0:
                            treasures.append(curLen + 1)
                        else:
                            if grid[nr][nc] == 2147483647 and ((nr, nc) not in visited):
                                visited.add((nr, nc))
                                queue.append((nr, nc, 1 + curLen))
                            elif grid[nr][nc] != -1:
                                treasures.append(curLen + 1 + grid[nr][nc])
            grid[i][j] = min(treasures)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2147483647:
                    bfs(i, j)

