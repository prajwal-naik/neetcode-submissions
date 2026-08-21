class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        visited = set()

        def dfs(cur, prev):
            if cur in visited:
                return True
            visited.add(cur)
            for child in adj[cur]:
                # if child == prev:
                #     continue
                if child != prev:
                    if not dfs(child, cur):
                        return False
            return True

        count = 0
        for i in range(n):
            if i not in visited:
                if dfs(i, -1) == True:
                    count += 1
        return count