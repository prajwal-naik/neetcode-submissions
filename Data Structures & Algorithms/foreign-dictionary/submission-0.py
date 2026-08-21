class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)

        for w in words:
            for c in w:
                graph[c]

        N = len(words)

        for i in range(N - 1):
            first = words[i]
            second = words[i + 1]
            minLen = min(len(first), len(second))
            if len(first) > len(second) and first[:minLen] == second[:minLen]:
                return ""

            for j in range(minLen):
                if first[j] != second[j]:
                    graph[first[j]].add(second[j])
                    break

        print(graph)

            
        numLetters = len(graph)
        UNVISITED, VISITING, VISITED = 0, 1, 2
        status = {}
        for c in graph:
            status[c] = UNVISITED

        print(status)

        def dfs(curLetter, res):
            if status[curLetter] == VISITING:
                return False
            
            if status[curLetter] == VISITED:
                return True

            status[curLetter] = VISITING
            for next in graph[curLetter]:
                if not dfs(next, res):
                    return False

            status[curLetter] = VISITED
            res.append(curLetter)
            return True

        resStr = []

        for c in graph:
            if not dfs(c, resStr):
                return ""

        return "".join(resStr)[::-1]

        