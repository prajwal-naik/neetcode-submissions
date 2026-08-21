class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count