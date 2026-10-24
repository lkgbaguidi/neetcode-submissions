class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupeAnagrams = {}
        for x in strs:
            sorted_x = "".join(sorted(x))
            if sorted_x in groupeAnagrams:
                groupeAnagrams[sorted_x].append(x)
            else:
                groupeAnagrams[sorted_x] = [x]
        return list(groupeAnagrams.values())
                

        