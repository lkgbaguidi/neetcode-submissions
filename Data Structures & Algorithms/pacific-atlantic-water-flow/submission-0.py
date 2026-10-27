class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(start_row, start_col):
            visited = set()
            q = deque()

            for c in range(cols):
                if (start_row, c) not in visited:
                    visited.add((start_row, c))
                    q.append((start_row, c))
            for r in range(rows):
                if (r, start_col) not in visited:
                    visited.add((r, start_col))
                    q.append((r, start_col))

            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                            and (nr, nc) not in visited
                            and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return visited

        pacific = bfs(0, 0)
        atlantic = bfs(rows - 1, cols - 1)

        return [[r, c] for r, c in pacific & atlantic]