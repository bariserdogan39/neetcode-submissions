class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        element = ""
        for i in strs:
            element += str(len(i)) + "#" + i

        return element

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        element, i = [], 0

        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            element.append(s[j+1:j+1+length])
            i =j+1+length

        return element





