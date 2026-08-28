from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = defaultdict(list)

        for element in strs:   
            key = tuple(sorted(element))
            group[key].append(element)
        
        return list(group.values())