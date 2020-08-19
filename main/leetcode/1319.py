class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        graph = [[] for _ in range(n)]

        for [a, b] in connections:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n

        def dfs(cur):
            visited[cur] = True

            for child in graph[cur]:
                if not visited[child]:
                    dfs(child)

        num_cc = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                num_cc += 1

        return num_cc - 1
