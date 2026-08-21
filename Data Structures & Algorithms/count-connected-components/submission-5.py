class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        print("Graph: ", graph)
        visited = set()
        def dfs(node):
            stack = deque()
            stack.append(node)
            visited.add(node)
            while stack:
                current = stack.pop()
                visited.add(current)
                for c in graph[current]:
                    if c not in visited:
                        stack.append(c)
                        visited.add(c)
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count
            
            