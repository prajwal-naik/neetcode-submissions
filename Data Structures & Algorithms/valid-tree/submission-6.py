class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for i in range(n)]
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        UNVISITED, VISITING, VISITED  = 0, 1, 2
        status = [UNVISITED for i in range(n)]

        def dfs(i, parent):
            if status[i] == VISITING:
                return False
            if status[i] == VISITED:
                return True
            status[i] = VISITING
            for child in graph[i]:
                if child != parent:
                    if not dfs(child, i):
                        return False
            status[i] = VISITED
            return True

        if not dfs(0, -1):
            return False
        for i in range(n):
            if status[i] == UNVISITED:
                return False
        return True