class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for n in s:
            if n - 1 not in s:          # n est le DÉBUT d'une suite
                length = 1
                while n + length in s:  # on avance tant que la suite continue
                    length += 1
                best = max(best, length)

        return best