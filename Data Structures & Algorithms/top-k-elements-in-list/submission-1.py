class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         
        d = {}

        for num in nums:
            d[num] = 1 + d.get(num, 0)
        
        elements = []
        for num, cnt in d.items():
            elements.append([cnt, num])
        elements.sort()

        cnt = []
        while len(cnt)<k:
            cnt.append(elements.pop()[1])

        return cnt


