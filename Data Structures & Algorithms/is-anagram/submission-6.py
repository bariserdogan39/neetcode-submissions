class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        lis = [0]*26

        for i in range(len(s)):
            lis[ord(s[i]) - ord("a")] += 1
            lis[ord(t[i]) - ord("a")] -= 1

        for i in lis:
            if i != 0:
                return False
        return True
        