class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        cnt, code = [], []
        for i in strs:
            cnt.append(len(i))
        for i in cnt:
            code.append(str(i))
            code.append(",")
        code.append("#")
        code.extend(strs)
        return "".join(code)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        cnt, code, i = [], [],0
        while s[i] != "#":
            j=i
            while s[j] != ",":
                j+=1
            cnt.append(int(s[i:j]))
            i=j+1

        i+=1
        for c in cnt:
            code.append(s[i:i+c])
            i +=c
        return code









