class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        l_max = []
        res = []

        for x in nums:
            elements [x] = elements.get(x, 0) + 1
        
        for t,v in elements.items():
            l_max.append([v,t])
        
        l_max.sort()

        while len(res) < k:
            res.append(l_max.pop()[1])
        return res

        