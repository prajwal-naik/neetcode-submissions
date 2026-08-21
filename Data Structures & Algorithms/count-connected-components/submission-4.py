class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        visited = set()
        
        def dfs(i):
            visited.add(i)
            if len(graph[i]) != 0:
                for c in graph[i]:
                    if c not in visited:
                        dfs(c)

            

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count