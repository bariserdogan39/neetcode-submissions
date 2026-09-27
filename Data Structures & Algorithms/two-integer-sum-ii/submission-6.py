class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        d = defaultdict(int)

        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if d[tmp]:
                return [d[tmp], i+1]
            d[numbers[i]] = i + 1 
        return []




        

