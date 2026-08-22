class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        visited = set()

        def dfs(cur):
            visited.add(cur)
            for child in graph[cur]:
                if child not in visited:
                    dfs(child)
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res