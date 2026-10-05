class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lists = []
        for i in nums:
            if i not in lists:
                lists.append(i)
        return len(lists) != len(nums)
        