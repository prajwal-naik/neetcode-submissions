class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for n in graph[node]:
                if n != parent:
                    if not dfs(n, node):
                        return False
            return True

        if not dfs(0, -1):
            return False
        if len(visited) != n:
            return False
        return True
