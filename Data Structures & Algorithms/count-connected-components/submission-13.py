class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        visited = set()

        def util(cur):
            visited.add(cur)
            for child in graph[cur]:
                if child not in visited:
                    util(child)

        res = 0
        for node in range(n):
            if node not in visited:
                res += 1
                util(node)

        return res
