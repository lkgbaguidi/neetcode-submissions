class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        best = nums[0]

        for x in nums:
            if cur < 0:
                cur = 0
            cur += x
            best = max(best, cur)

        return best
        