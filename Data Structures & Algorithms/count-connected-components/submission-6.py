class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        def dfs(cur, parent):
            if cur in visited:
                return
            visited.add(cur)
            for neigh in graph[cur]:
                if neigh != cur:
                    dfs(neigh, cur)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i, -1)

        return res