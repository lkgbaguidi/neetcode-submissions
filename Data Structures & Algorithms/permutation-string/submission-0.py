class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        goal = {}
        for x in s1:
            goal[x] = goal.get(x, 0) + 1

        seen = {}
        l = 0
        for r in range(len(s2)):
            seen[s2[r]] = seen.get(s2[r], 0) + 1      # 1) la lettre entre

            if r - l + 1 == len(s1):                   # 2) la fenêtre a la bonne taille
                if seen == goal:
                    return True
                seen[s2[l]] -= 1                       # 3) la lettre de gauche sort
                if seen[s2[l]] == 0:
                    del seen[s2[l]]                    # on supprime les clés à 0
                l += 1

        return False