class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        a = [0] * 26
        b = [0] * 26
        for i in range(len(s1)):
            a[ord(s1[i]) - ord('a')] += 1
            b[ord(s2[i]) - ord('a')] += 1

        if a == b:
            return True

        for r in range(len(s1), len(s2)):
            b[ord(s2[r]) - ord('a')] += 1                 # entre
            b[ord(s2[r - len(s1)]) - ord('a')] -= 1       # sort
            if a == b:
                return True
        return False