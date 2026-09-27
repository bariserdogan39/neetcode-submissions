class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        d = defaultdict(int)

        for num in nums:
            if not d[num]:
                d[num] = d[num-1] + d[num+1] + 1
                d[num - d[num-1]] = d[num]
                d[num + d[num+1]] = d[num]

            res = max(d[num], res)
        return res