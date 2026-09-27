class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = "".join(h for h in s if h.isalnum()).lower()
        
        for i in range(len(res)//2):

            if res[i] !=res[len(res)-1-i]:
                return False
            
        return True
                
        