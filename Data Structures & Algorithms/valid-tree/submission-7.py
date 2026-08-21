class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        UNVISITED, VISITING, VISITED = 0, 1, 2
        status = [UNVISITED] * n

        def dfs(cur, parent):
            if status[cur] == VISITING:
                return False
            if status[cur] == VISITED:
                return True
            status[cur] = VISITING
            for neigh in graph[cur]:
                if neigh != parent:
                    if not dfs(neigh, cur):
                        return False
            status[cur] = VISITED
            return True

        if not dfs(0, -1):
            return False
        for i in range(n):
            if status[i] == UNVISITED:
                return False
        return True


    