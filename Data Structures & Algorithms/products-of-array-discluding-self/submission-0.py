class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        indices = [i for i, x in enumerate(nums) if x == 0]
        if indices != [] :
            if len(indices) > 1:
                return [0 for i in range(len(nums))]
            else:
                nbre= 1
                indice = indices[0]
                for i in range(len(nums)) :
                    if i != indice:
                        nbre = nbre* nums[i]
                res = [0 for i in range(len(nums))]
                res[indice] = nbre
                return res
        else:
            nbre = 1
            for x in nums:
                nbre *=x
            res = [nbre for i in range(len(nums))]
            for i in range(len(res)):
                res[i] //= nums[i]
            return res
            


           


