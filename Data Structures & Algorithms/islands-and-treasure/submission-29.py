class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        visited = set()
        
        while(queue):
            cur_r, cur_c, curDis = queue.popleft()
            visited.add((cur_r, cur_c))
            for dr, dc in directions:
                nr, nc = cur_r + dr, cur_c + dc
                if (nr in range(ROWS) and nc in range(COLS)) and \
                ((nr, nc) not in visited) and \
                (grid[nr][nc] != -1):
                    visited.add((nr, nc))
                    queue.append((nr, nc, curDis + 1))
                    grid[nr][nc] = min(grid[nr][nc], curDis + 1)
            
        