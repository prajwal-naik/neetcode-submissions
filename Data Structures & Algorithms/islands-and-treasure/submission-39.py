class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        heap = deque()
        # costs = defaultdict(lambda : float('inf'))
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    # costs[(i, j)] = 0
                    heap.append((0, i, j))

        while heap:
            curCost, cr, cc = heap.popleft()
            if curCost > grid[cr][cc]:
                continue
            # costs[(cr, cc)] = curCost
            grid[cr][cc] = curCost
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if (
                    nr in range(ROWS) and 
                    nc in range(COLS) and 
                    grid[nr][nc] != -1 and 
                    curCost + 1 < grid[nr][nc]
                ):
                    heap.append((curCost + 1, nr, nc))



    