class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)

        for word in words:
            for c in word:
                graph[c]

        N = len(words)
        for i in range(N - 1):
            word1 = words[i]
            word2 = words[i + 1]
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    break

        print(graph)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        status = defaultdict(lambda : UNVISITED)
        res = []
        def dfs(cur):
            if status[cur] == VISITING:
                return False
            if status[cur] == VISITED:
                return True

            print("starting DFS")

            status[cur] = VISITING
            for child in graph[cur]:
                if not dfs(child):
                    return False
            status[cur] = VISITED
            res.append(cur)
            return True

        for c in graph:
            if not dfs(c):
                return ""

        return "".join(res[::-1])















