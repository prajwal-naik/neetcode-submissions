class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = [[] for i in range(n)]
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for d in adj[node]:
                if d == prev:
                    continue
                if not dfs(d, node):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)

            