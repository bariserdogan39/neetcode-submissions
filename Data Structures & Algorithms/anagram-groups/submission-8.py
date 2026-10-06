class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        d = defaultdict(list)

        for i in strs:
            order = tuple(sorted(i))
            d[order].append(i)
        
        return list(d.values())