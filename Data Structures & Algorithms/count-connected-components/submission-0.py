class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node)
            for nxt in graph[node]:
                if nxt not in visited:
                    dfs(nxt)

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count