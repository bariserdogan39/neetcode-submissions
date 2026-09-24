class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        
        for i in range(len(strs)):
            default = tuple(sorted(strs[i]))
            d[default].append(strs[i])

        return list(d.values())

        