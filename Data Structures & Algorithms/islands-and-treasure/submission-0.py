class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def bfs(r, c):
            treasures = []
            visited = set()
            que = deque()
            que.append((r, c, 0))
            
            while len(que) != 0:
                cur_r, cur_c, cur_len = que.popleft()
                for dr, dc in dirs:
                    new_r, new_c = cur_r + dr, cur_c + dc
                    if new_r in range(ROWS) and new_c in range(COLS) and \
                        grid[new_r][new_c] == 0:
                        treasures.append(cur_len + 1)
                    else:
                        if new_r in range(ROWS) and new_c in range(COLS) \
                        and ((new_r, new_c) not in visited):
                            if (grid[new_r][new_c] == 2147483647):
                                que.append((new_r, new_c, cur_len + 1))
                                visited.add((new_r, new_c))
                            elif (grid[new_r][new_c] != -1):
                                treasures.append(cur_len + 1 + grid[new_r][new_c])

            grid[r][c] = min(treasures)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2147483647:
                    bfs(i, j)

