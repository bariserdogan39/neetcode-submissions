class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        
        liste = []
        for num , i in d.items():
            liste.append([i,num])
        
        liste.sort()

        res = []
        while len(res)<k:
            res.append(liste.pop()[1])
        return res
