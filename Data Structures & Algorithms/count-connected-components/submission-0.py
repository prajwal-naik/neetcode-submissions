class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        graph = [[] for i in range(n)]
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        def dfs(node, prev):
            if node in visited:
                return
            visited.add(node)
            for child in graph[node]:
                if child == prev:
                    continue
                if child not in visited:
                    dfs(child, node)
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i, -1)
        return res
            