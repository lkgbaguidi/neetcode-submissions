class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses

        def has_cycle(c):
            if state[c] == 1:
                return True
            if state[c] == 2:
                return False
            state[c] = 1
            for nxt in graph[c]:
                if has_cycle(nxt):
                    return True
            state[c] = 2
            return False

        return not any(has_cycle(c) for c in range(numCourses))
        