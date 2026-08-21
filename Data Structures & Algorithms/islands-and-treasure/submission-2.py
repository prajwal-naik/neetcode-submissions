class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def bfs(i, j):
            visited = set()
            queue = deque()
            treasures = []
            queue.append((i, j, 0))
            while queue:
                cur_r, cur_c, cur_len = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + cur_r, dc + cur_c
                    if nr in range(ROWS) and nc in range(COLS):
                        if grid[nr][nc] == 0:
                            treasures.append(cur_len + 1)
                        else:
                            if (nr, nc) not in visited:
                                if (grid[nr][nc] == 2147483647):
                                    queue.append((nr, nc, cur_len + 1))
                                    visited.add((nr, nc))
                                elif (grid[nr][nc] != -1):
                                    treasures.append(cur_len + 1 + grid[nr][nc])

            
            grid[i][j] = min(treasures)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2147483647:
                    
                    bfs(i, j)