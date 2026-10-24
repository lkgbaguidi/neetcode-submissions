class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r = len(numbers) - 1
        res = numbers[l] + numbers[r]
        while res != target:
            if res > target:
                r -= 1
            else:
                l+=1
            res = numbers[l] + numbers[r]
            
        return [l +1,r + 1 ]

        