from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        sub = {}
        for i in s1:
            sub[i] = 1 + sub.get(i, 0)
        n = len(sub)

        for i in range(len(s2)):
            sub2, count = {}, 0
            for j in range(i,len(s2)):
                sub2[s2[j]] = 1 + sub2.get(s2[j], 0)

                if sub.get(s2[j], 0)< sub2[s2[j]]:
                    break
                if sub[s2[j]] == sub2[s2[j]]:
                    count += 1
                if count == n:
                    return True
        return False 



