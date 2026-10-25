class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}                       # caractère -> dernier indice vu
        l = 0
        best = 0

        for r, c in enumerate(s):
            if c in last and last[c] >= l:
                l = last[c] + 1         # on saute juste après l'ancien doublon
            last[c] = r
            best = max(best, r - l + 1)

        return best