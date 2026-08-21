class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for i in range(n)]

        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        visited = set()

        def dfs(current, parent):
            if current in visited:
                return False
            visited.add(current)
            for child in graph[current]:
                if child == parent:
                    continue
                if not dfs(child, current):
                    return False
            return True

        valid = dfs(0, -1)
        return len(visited) == n and valid